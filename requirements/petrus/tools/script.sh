#!/bin/sh

python manage.py makemigrations
python manage.py migrate
# gunicorn --bind 0.0.0.0:8001 petrus_project.wsgi:application
python manage.py runserver 0.0.0.0:8001
