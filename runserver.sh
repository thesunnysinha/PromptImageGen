#!/bin/bash
script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$script_directory/backend"


python manage.py deletemigrations

python manage.py makemigrations image_generation

python manage.py setupapplication

python manage.py runserver 0.0.0.0:8000