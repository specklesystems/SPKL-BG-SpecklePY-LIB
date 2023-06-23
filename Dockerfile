FROM python:3.11-slim

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .
RUN poetry install --only main