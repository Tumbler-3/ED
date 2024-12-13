FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations \
    && python manage.py migrate

COPY . /app
RUN python manage.py collectstatic --noinput

ENTRYPOINT [ "gunicorn", "ED.wsgi", "-b", "0.0.0.0:6800"]