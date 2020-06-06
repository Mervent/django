#!/bin/bash -e


pip-compile -q $dep requirements.in
pip-compile -q $dep requirements-dev.in

pip-sync requirements.txt requirements-dev.txt
