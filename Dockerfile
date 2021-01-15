FROM python:3.8.3-alpine

RUN mkdir -p /usr/src/el_royale

WORKDIR /usr/src/el_royale

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/el_royale/entrypoint.sh"]