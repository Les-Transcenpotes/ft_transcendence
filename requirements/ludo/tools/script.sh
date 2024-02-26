#!/bin/sh


pip install -r shared/shared_requirements.txt 2> /dev/null 1> /dev/null
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8006
# daphne -b :: -p 8006 ludo_project.asgi:application
# gunicorn --bind 0.0.0.0:8006 ludo_project.wsgi:application
