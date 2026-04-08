

FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn pydantic gradio

CMD ["python", "src/app.py"]

