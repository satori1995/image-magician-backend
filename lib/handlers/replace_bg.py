"""
替换背景
"""
from io import BytesIO
import httpx
from PIL import Image
import numpy as np
from sanic import Request, raw
from rembg import remove, new_session
from lib.app_core import app
from lib.app_core.global_context import global_context

HTTPX_CLIENT = httpx.AsyncClient(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"},
)


@app.post("/show_bg")
async def show_bg(request: Request):
    prompt = global_context.request_data.json.get("prompt", "")
    cursor = global_context.request_data.json.get("cursor", 0)
    res = await HTTPX_CLIENT.post(
        "https://lexica.art/api/infinite-prompts",
        json={"text": prompt, "model": "lexica-aperture-v3.5", "searchMode": "images", "source": "search",
              "cursor": cursor}
    )
    data = res.json()
    # 下一批图片的光标
    next_cursor = data["nextCursor"]
    # 所有的图片
    images = [
        {
            "id": image["id"],
            "url": f"https://image.lexica.art/md2/{image['id']}",
            "width": image["width"],
            "height": image["height"]
        }
        for image in data["images"]
    ]
    global_context.response_data.set(200, {"cursor": next_cursor, "images": images})
    return global_context.response_data.response


@app.post("/replace_bg")
async def replace_bg(request: Request):
    upload_files = global_context.request_data.files
    # 获取上传的文件
    target_file = list(upload_files.values())[0][0]
    # 图像处理，移除背景
    output_bytes = remove(target_file.body, alpha_matting=True, session=new_session("isnet-general-use"))
    output_image = Image.open(BytesIO(output_bytes))
    # 要替换的背景文件
    image = global_context.request_data.form
    resp = await HTTPX_CLIENT.get(f"https://image.lexica.art/full_jpg/{image.get('id')}")
    content = resp.content
    bg_image = Image.open(BytesIO(content))
    # 将处理后的图像贴到背景文件上，但要先处理尺寸
    width_ratio, height_ratio = bg_image.width / output_image.width, bg_image.height / output_image.height
    # 说明背景图片的宽度或高度不够，不足以匹配原始图像，那么要将背景图片放大
    if width_ratio < 1 or height_ratio < 1:
        expand_ratio = 1 / min([width_ratio, height_ratio])
        bg_image = bg_image.resize((int(bg_image.width * expand_ratio), int(bg_image.height * expand_ratio)))
    # 从中心位置对背景图片进行截取，使其和原始图片的形状保持一致
    left_width_padding = (bg_image.width - output_image.width) // 2
    left_height_padding = (bg_image.height - output_image.height) // 2
    bg_image_array = np.array(bg_image)[
                     left_height_padding: left_height_padding + output_image.height,
                     left_width_padding: left_width_padding + output_image.width,
                     ]
    bg_image = Image.fromarray(bg_image_array)
    # 粘贴
    final_image = Image.alpha_composite(bg_image.convert("RGBA"), output_image)
    # 导出字节流
    buf = BytesIO()
    final_image.save(buf, format="png")
    return raw(
        buf.getvalue(),
        headers={"Content-Disposition": f"inline; filename=precessed_image.png"},
        content_type="image/png",
    )



