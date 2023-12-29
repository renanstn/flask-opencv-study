FROM python:3.9 AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --upgrade pip && \
    pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
COPY . /app/

FROM base AS development
CMD [ "flask", "--app", "main", "run", "--host=0.0.0.0", "--debug" ]

FROM base AS production
RUN chmod +x run_prod.sh
CMD [ "./run_prod.sh" ]
