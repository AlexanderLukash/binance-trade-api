# Використовуємо офіційний образ Python
FROM python:3.13.2-slim-bullseye

WORKDIR /app

RUN pip install uv


COPY pyproject.toml .

RUN uv pip install --system .

ENV PYTHONPATH /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY /src/* .
