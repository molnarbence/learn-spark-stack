FROM python:3.10-bullseye AS spark-base

# Install python deps
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY uv.lock pyproject.toml hello.py ./

ENTRYPOINT [ "bash" ]