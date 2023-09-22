#!/bin/bash
set -e

source .env.development && python manage.py runserver localhost:8000
