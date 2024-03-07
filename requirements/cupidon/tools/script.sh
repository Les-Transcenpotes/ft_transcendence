#!/bin/sh

python manage.py runserver 0.0.0.0:8003
# gunicorn --bind 0.0.0.0:8003 cupidon_project.wsgi:application
