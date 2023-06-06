FROM paperspace/fastapi-deployment:latest

WORKDIR /app

COPY main.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]