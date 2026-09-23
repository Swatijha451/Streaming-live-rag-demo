FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python scripts/build_index.py
CMD ["sh","-c","python scripts/run_replay.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
