#!/bin/sh

python manage.py runserver 0.0.0.0:8001
# gunicorn --bind 0.0.0.0:8001 alfred_project.wsgi:application
