"""
移除背景
"""
from rembg import remove, new_session
from sanic import Request, raw
from lib.app_core import app
from lib.app_core.global_context import global_context


@app.post("/remove_bg")
async def remove_bg(request: Request):
    upload_files = global_context.request_data.files
    # 获取上传的文件
    target_file = list(upload_files.values())[0][0]
    # 图像处理
    output_bytes = remove(target_file.body, alpha_matting=True, session=new_session("isnet-general-use"))
    return raw(
        output_bytes,
        headers={"Content-Disposition": f"inline; filename=precessed_image.png"},
        content_type="image/png",
    )





