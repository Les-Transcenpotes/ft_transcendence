#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8002
# gunicorn --bind 0.0.0.0:8002 coubertin_project.wsgi:application
