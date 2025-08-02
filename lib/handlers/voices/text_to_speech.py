"""
文本转语音
"""
import os
from pathlib import Path
import httpx
from sanic import Request, raw
from lib.app_core import app
from lib.app_core.global_context import global_context

API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLkuIfmmI7nj6AiLCJVc2VyTmFtZSI6IuS4h-aYjuePoCIsIkFjY291bnQiOiIiLCJTdWJqZWN0SUQiOiIxOTQyODI0MDc0MzYzMjc3NTQwIiwiUGhvbmUiOiIiLCJHcm91cElEIjoiMTk0MjgyNDA3NDM1NDg4ODkzMiIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6InNoaWluYW1hc2hpcm8xNjNAZ21haWwuY29tIiwiQ3JlYXRlVGltZSI6IjIwMjUtMDgtMDEgMTU6NTA6MDEiLCJUb2tlblR5cGUiOjEsImlzcyI6Im1pbmltYXgifQ.gLYULTVktYbNbSt5O-rQnyGW-jy3-rFjBKlzSdZhmeB0_80WojnbBoFZJWE0BwXybIIFPmhSIFc2O9m4_tXYtdZIdO-9HWtDEaqpB2CTBClcX77I9w8sUOW6451RchhOQQS5C6NFQmF_4zglBrR_3WFDRgi4eRU9t5hA2oXTSbtkPRhNzWXHLOPVzAta6PFiZwEaDkm3Vk8K_npXSFz-y2NkEonFx1qqcsn65PQmiQ2jS6Y3K7iwwAA8PdBEyAwjL8C_fChL9smlJYa-eTK6TRCzEVpzR9ts1oS0gRf7cUf_Wjz7o8NFpAxrGV44uTbX2ZkBZDCywTnlc1cnJ21aVg"
GROUP_ID = "1942824074354888932"
HTTPX_CLIENT = httpx.AsyncClient(
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {API_KEY}",
    },
    timeout=10
)


@app.post("/text_to_speech")
async def text_to_speech(request: Request):
    endpoint = f"https://api.minimax.io/v1/t2a_v2?GroupId={GROUP_ID}"
    payload = {
        "model": "speech-02-hd",
        "text": global_context.request_data.json["text"],
        "voice_setting": {
            "voice_id": global_context.request_data.json["voice_id"],
            "speed": global_context.request_data.json["speed"],
            "vol": global_context.request_data.json["vol"],
            "pitch": global_context.request_data.json["pitch"],
            "emotion": global_context.request_data.json["emotion"],
        },
        "audio_setting": {
            "sample_rate": global_context.request_data.json["sample_rate"],
            "bitrate": global_context.request_data.json["bitrate"],
            "format": global_context.request_data.json["format"],
            "channel": global_context.request_data.json["channel"],
        }
    }
    if payload["voice_setting"]["emotion"] == "auto":
        payload["voice_setting"].pop("emotion")
    resp = await HTTPX_CLIENT.post(endpoint, json=payload)
    global_context.response_data.set(200, resp.json())
    return global_context.response_data.response


@app.get("/audio_preview")
async def audio_preview(request: Request):
    voice_id = global_context.request_data.query["voice_id"][0]
    file = Path(__file__).parent / "audio_preview" / voice_id
    if file.exists():
        audio = file.read_text("utf-8")
    else:
        endpoint = f"https://api.minimax.io/v1/t2a_v2?GroupId={GROUP_ID}"
        payload = {
            "model": "speech-02-hd",
            "text": "您好，欢迎使用 AI 配音服务，请告诉我您想说的话吧。",
            "voice_setting": {
                "voice_id": voice_id,
            }
        }
        resp = await HTTPX_CLIENT.post(endpoint, json=payload)
        audio = resp.json()["data"]["audio"]
        file.write_text(audio, "utf-8")
    global_context.response_data.set(200, {"audio": audio})
    return global_context.response_data.response




