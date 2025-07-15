"""
模糊背景
"""
from io import BytesIO
from PIL import Image, ImageFilter
from rembg import remove, new_session
from sanic import Request, raw
from lib.app_core import app
from lib.app_core.global_context import global_context


@app.post("/blur_bg")
async def blur_bg(request: Request):
    upload_files = global_context.request_data.files
    # 获取上传的文件
    target_file = list(upload_files.values())[0][0]
    # 图像处理，移除背景
    output_bytes = remove(target_file.body, alpha_matting=True, session=new_session("isnet-general-use"))
    output_image = Image.open(BytesIO(output_bytes))
    # 原始图像
    original_image = Image.open(BytesIO(target_file.body))
    # 创建背景模糊版本
    radius = int(global_context.request_data.query["radius"][0])
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=radius))
    # 将去掉背景的主体贴到模糊背景上
    final_image = Image.alpha_composite(blurred_image.convert("RGBA"), output_image)
    # 导出字节流
    buf = BytesIO()
    final_image.save(buf, format="png")
    return raw(
        buf.getvalue(),
        headers={"Content-Disposition": f"inline; filename=precessed_image.png"},
        content_type="image/png",
    )


