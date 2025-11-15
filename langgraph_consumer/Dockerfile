FROM python:3.13-slim
LABEL authors="thalestmm"

RUN apt-get update && apt-get install -y gcc
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir uv

ENV PATH="/root/.cargo/bin:${PATH}"

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

ENV PATH="/app/.venv/bin:${PATH}"

CMD ["uv", "run", "celery", "-A", "app.worker.tasks", "worker", "--loglevel=info"]