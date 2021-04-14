#!/bin/bash -e

set -x

virtualenv .venv
. .venv/bin/activate

pip install --upgrade pip
pip install poetry
poetry install
