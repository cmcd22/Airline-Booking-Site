FROM python:3.9-bullseye
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  pip install --upgrade pip
COPY requirements.txt /app
RUN  pip install -r requirements.txt

COPY . /app/
RUN rm -r venv/

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
