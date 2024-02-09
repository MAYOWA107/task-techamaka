ARG PYTHON_VERSION=3.9-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt



ENV SECRET_KEY "hXRPUhepBuJAN6tr2IW073ZFjK2g722E1qYT0NtL9tqsUM1Lnq"
ENV SECRET_KEY "non-secret-key-for-building-purposes"

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "SHMS.wsgi"]

