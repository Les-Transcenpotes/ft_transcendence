#!/bin/sh


python manage.py runserver 0.0.0.0:8006
# daphne -b :: -p 8006 ludo_project.asgi:application
# gunicorn --bind 0.0.0.0:8006 ludo_project.wsgi:application
