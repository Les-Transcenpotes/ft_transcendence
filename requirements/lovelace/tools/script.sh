#!/bin/sh

python manage.py runserver 0.0.0.0:8005
# gunicorn --bind 0.0.0.0:8005 lovelace_project.wsgi:application
