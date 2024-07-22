#!/bin/bash
python3 manage.py makemigrations users
python3 manage.py migrate
python3 manage.py runserver