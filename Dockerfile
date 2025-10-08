FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ .

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update && apt install -y build-essential

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --compile-bytecode

CMD ["uv", "run", "python", "main.py"]
