#!/bin/sh

python manage.py runserver 0.0.0.0:8004
# gunicorn --bind 0.0.0.0:8004 hermes_project.wsgi:application
