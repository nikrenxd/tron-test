FROM python:3.12-alpine3.20

COPY --from=ghcr.io/astral-sh/uv:0.5.7 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# env variable for installing dependencies inside container
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app/

# install dependencies
COPY ./pyproject.toml ./uv.lock /app/
RUN uv pip install -r pyproject.toml

COPY . /app/