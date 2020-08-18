FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0

RUN python -m pip install --upgrade pip && \
    pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && \
    pipenv lock --requirements > requirements.txt

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r /tmp/requirements.txt && \
    apk --purge del .build-deps

COPY . .

CMD ["gunicorn", "seamless.wsgi:application"]