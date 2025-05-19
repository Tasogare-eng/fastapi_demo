# FastAPIサンプル

```bash
mkdir fastapi_demo
cd fastapi_-_demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### docker
```bash
docker-compose up --build -d
```