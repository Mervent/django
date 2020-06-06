#!/bin/bash -e

set -x

virtualenv .venv
. .venv/bin/activate

pip install --upgrade pip
pip install pip-tools

(cd ./requirements && sh update.sh)

(cd src && python manage.py collectstatic)
