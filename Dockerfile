FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0
COPY Pipfile* ./seamless/
WORKDIR seamless
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pipenv install --deploy && \
    apk --purge del .build-deps
COPY . .
