"""
图像动漫化
"""
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from sanic import Request, raw
from lib.app_core import app
from lib.app_core.global_context import global_context


@app.post("/animate_image")
async def animate_image(request: Request):
    upload_files = global_context.request_data.files
    target_file = list(upload_files.values())[0][0]
    print(global_context.request_data.form["style"])
    # 创建图像数组
    im = np.asarray(Image.open(BytesIO(target_file.body)))
    # 1. 双边滤波去噪同时保持边缘
    smooth = cv2.bilateralFilter(im, 9, 200, 200)
    # 2. 创建边缘mask
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 8)
    # 3. 颜色减少（简单量化）
    # 将每个颜色通道的值减少到较少的级别
    div = 64
    smooth = smooth // div * div
    # 4. 转换边缘为3通道并与图像结合
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(smooth, edges)
    buf = BytesIO()
    Image.fromarray(cartoon).save(buf, format="PNG")
    return raw(
        buf.getvalue(),
        headers={"Content-Disposition": f"inline; filename=precessed_image.png"},
        content_type="image/png",
    )





