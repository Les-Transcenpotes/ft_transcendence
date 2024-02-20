#!/bin/sh


pip install -r shared/shared_requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8005
# gunicorn --bind 0.0.0.0:8005 ludo_project.wsgi:application
