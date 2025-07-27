FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
COPY ./pyproject.toml /app/
COPY ./src /app/src
RUN uv sync

ENTRYPOINT ["uv", "run"]
CMD ["main.py"]
