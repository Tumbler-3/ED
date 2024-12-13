FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ED.settings

RUN mkdir -p /app/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "44.226.145.213:8000"]