FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml ./

RUN pip install uv

RUN uv pip install --system \
    fastapi \
    uvicorn \
    sqlalchemy \
    psycopg[binary] \
    alembic \
    python-dotenv

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

