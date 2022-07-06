FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /random_api_json
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
