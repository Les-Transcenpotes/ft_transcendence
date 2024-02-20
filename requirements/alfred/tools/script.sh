#!/bin/sh

pip install -r shared/shared_requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
# gunicorn --bind 0.0.0.0:8001 alfred_project.wsgi:application
