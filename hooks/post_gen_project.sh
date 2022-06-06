#!/bin/bash -e

set -x

python -m virtualenv .venv
. .venv/bin/activate

pip install --upgrade pip
pip install poetry
poetry install
