#!/bin/sh


python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8005
docker run -p 6379:6379 -d redis:5
# gunicorn --bind 0.0.0.0:8005 ludo_project.wsgi:application
