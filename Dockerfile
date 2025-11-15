FROM python:3.12-slim

RUN pip install poetry

# Poetry ставит пакеты прямо в системный Python
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
#RUN poetry install --no-interaction --no-ansi
RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["python", "main.py"]

