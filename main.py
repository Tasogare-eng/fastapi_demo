# main.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx  # 非同期 HTTP クライアント

load_dotenv()
app = FastAPI()

# CORS 設定（必要に応じて調整）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/weather")
async def get_weather(
    city: str = Query(
        ..., 
        title="都市名", 
        description="天気を取得したい都市名（例: Tokyo）"
    )
) -> dict:
    """
    /weather?city=<都市名> で呼び出された際、
    OpenWeatherMap API から指定都市の現在の天気を取得してそのまま JSON で返します。
    環境変数 OPENWEATHER_API_KEY に API キーを設定してください。
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500, 
            detail="サーバー設定エラー：OPENWEATHER_API_KEY が設定されていません"
        )

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",   # 摂氏で取得
        "lang": "ja",        # 日本語の説明文
    }

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)

    if resp.status_code != 200:
        # OpenWeatherMap 側のエラーをそのまま返す
        detail = resp.json().get("message", "Unknown error")
        raise HTTPException(status_code=resp.status_code, detail=detail)

    return resp.json()