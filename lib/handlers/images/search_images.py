"""
查询壁纸，来自于 https://lexica.art/
"""
import httpx
from sanic import Request, raw
from lib.app_core import app
from lib.app_core.global_context import global_context

HTTPX_CLIENT = httpx.AsyncClient(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"},
    timeout=10
)


@app.post("/search_images")
async def search_images(request: Request):
    prompt = global_context.request_data.json.get("prompt", "")
    cursor = global_context.request_data.json.get("cursor", 0)
    # 获取图片
    res = await HTTPX_CLIENT.post(
        "https://lexica.art/api/infinite-prompts",
        json={"text": prompt, "cursor": cursor, "model": "lexica-aperture-v3.5",
              "searchMode": "images", "source": "search"}
    )
    data = res.json()
    # 下一批图片的光标
    next_cursor = data["nextCursor"]
    # 拿到图片对应的提示词
    prompts = {prompt["id"]: prompt for prompt in data["prompts"]}
    # 图片属性
    images = [
        {
            "image_id": image["id"],
            "prompt": prompts[image["promptid"]]["prompt"],
            "thumb_url": f"https://image.lexica.art/md2/{image['id']}",
            "hd_url": f"https://image.lexica.art/full_jpg/{image['id']}",
            "width": image["width"],
            "height": image["height"]
        }
        for image in data["images"]
    ]
    global_context.response_data.set(200, {"cursor": next_cursor, "images": images})
    return global_context.response_data.response


@app.post("/get_image")
async def get_images(request: Request):
    image_url = global_context.request_data.json["image_url"]
    resp = await HTTPX_CLIENT.get(image_url)
    return raw(
        resp.content,
    )

