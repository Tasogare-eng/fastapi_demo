# FastAPIサンプル

```bash
mkdir fastapi_demo
cd fastapi_-_demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## API
Openweatehermap API
.envに設定
OPENWEATHER_API_KEY={YOUR API KEY}

### docker(FastAPI+nginx+uvicorn)
```bash
docker-compose up --build -d
```