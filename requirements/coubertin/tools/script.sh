#!/bin/sh

python manage.py migrate
gunicorn --bind 0.0.0.0:8000 coubertin_project.wsgi:application
