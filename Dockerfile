FROM paperspace/fastapi-deployment:latest

WORKDIR /app

COPY app ./
COPY requirements.txt ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]