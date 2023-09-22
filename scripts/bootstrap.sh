#!/bin/bash
set -e

test -f .env.development || cp .env.example .env.development

pipenv install --dev

! command -v pre-commit > /dev/null 2>&1 || pre-commit install

docker compose up -d

timeout 10 sh -c 'until pg_isready --host=localhost; do sleep 1; done'

pipenv run python manage.py migrate

docker compose stop
