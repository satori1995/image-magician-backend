"""
基础模型类
"""
from typing import Sequence
from sqlalchemy import and_, Result, BinaryExpression, BooleanClauseList, delete, update
from sqlalchemy.sql.selectable import Select
from sqlalchemy.ext.asyncio import AsyncSession
from lib.connectors import BaseModelType


class BaseModel(BaseModelType):
    """
    基础模型类，不映射任何表，只提供最基本、最通用的逻辑
    其它模型类需要继承 BaseModel
    """
    __abstract__ = True

    @classmethod
    async def get_records(cls,
                          session: AsyncSession,
                          conditions: dict | BinaryExpression | BooleanClauseList = None,
                          fields: Sequence = "*",
                          count: int = 1):
        """
        该方法的最初目的是通过主键获取单条记录，需要指定 pk_name 和 pk_value
        但考虑到扩展性，参数换成了 conditions，它是一个字典
        如果要基于主键获取记录，那么给 conditions 参数传入 {pk_name: pk_value} 即可
        当然此时除了主键还可以通过其它字段获取记录，并且同时支持多个字段，但只支持等值判断

        :param session: 通过调用 AsyncSession 创建
        :param conditions: 查询条件，如果等值判断不满足要求，那么也可以手动构建查询条件
        :param fields: 要获取哪些字段
        :param count: 获取的记录条数，默认为 1，如果指定为 -1，表示获取所有满足条件的记录
        :return: list[dict]
        """
        if type(fields) is not str:
            fields = [getattr(cls, field) for field in fields]
        query = Select(*fields).select_from(cls.__table__)
        if type(conditions) is dict:
            query = query.where(and_(*[getattr(cls, field) == value for field, value in conditions.items()]))
        elif conditions is not None:
            query = query.where(conditions)
        if count != -1:
            query = query.limit(count)
        result = await session.execute(query)
        data = cls.fetch_data(result)
        return data

    @classmethod
    async def insert_records(cls, session: AsyncSession, records: list[dict], pk_name: str = "id"):
        """
        插入记录，支持同时插入多条，返回插入后的每条记录的主键

        :param session: 异步 session
        :param records: 插入的记录
        :param pk_name: 主键字段名
        :return: list
        """
        obj_list = [cls(**record) for record in records]
        session.add_all(obj_list)
        await session.flush()  # 立即执行 SQL，但不提交事务
        return [getattr(obj, pk_name) for obj in obj_list]

    @classmethod
    async def delete_records(cls,
                             session: AsyncSession,
                             conditions: dict | BinaryExpression | BooleanClauseList):
        """
        删除记录

        :param session: 异步 session
        :param conditions: 条件
        :return: list
        """
        stmt = delete(cls)
        if type(conditions) is dict:
            stmt = stmt.where(and_(*[getattr(cls, field) == value for field, value in conditions.items()]))
        else:
            stmt = stmt.where(conditions)
        await session.execute(stmt)

    @classmethod
    async def update_records(cls,
                             session: AsyncSession,
                             conditions: dict | BinaryExpression | BooleanClauseList,
                             values: dict):
        """
        修改记录

        :param session: 异步 session
        :param conditions: 条件
        :param values: 修改后的值
        :return:
        """
        stmt = update(cls)
        if type(conditions) is dict:
            stmt = stmt.where(and_(*[getattr(cls, field) == value for field, value in conditions.items()]))
        else:
            stmt = stmt.where(conditions)
        stmt = stmt.values(values)
        await session.execute(stmt)

    @classmethod
    def fetch_data(cls, result: Result):
        fields = result.keys()
        values = result.fetchall()
        return [dict(zip(fields, value)) for value in values]


