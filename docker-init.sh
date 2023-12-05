#!/bin/sh

python3 manage.py migrate

gunicorn --bind :8000 notifyme.wsgi:application
