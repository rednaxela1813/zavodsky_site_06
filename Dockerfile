FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY  ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .
