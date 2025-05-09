FROM python:3.12.5-slim-bullseye
WORKDIR /app

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl wget file gcc git libffi-dev libpq-dev pkg-config \
    make python3-dev && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential

# Installing Poetry
RUN pip install --upgrade pip

COPY requirements.txt .

# Install python dependencies
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
