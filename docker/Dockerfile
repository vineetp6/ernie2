ARG PYTHON_VERSION
FROM python:3.12-slim-bookworm
RUN apt-get update && apt-get -y install gcc
COPY . .
RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -e .
