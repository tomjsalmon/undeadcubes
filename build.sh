#!/bin/bash

# Get in the virtualenv
source build-env/bin/activate

pip install -q -r build_requirements.txt

# Unit tests
echo Running unit tests ................
python3 -m unittest -q test_uc.py

# Static type checking
echo Type checking .....................
python3 -m mypy uc.py

# Linting
echo Linting ...........................
pylint --errors-only --rcfile .pylintrc uc.py
