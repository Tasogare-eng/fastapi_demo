# Dockerfile
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# 依存パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# Uvicorn のポートを開放
EXPOSE 8000

# Uvicorn で FastAPI を起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
