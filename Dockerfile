FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

COPY ./pyproject.toml /app/
COPY ./src /app/src
WORKDIR /app/src
RUN uv sync

ENTRYPOINT ["uv", "run"]
CMD ["main.py"]
