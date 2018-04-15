#!/bin/bash
mkdir .badges

# Run unit tests and generate SVG
python3 -m unittest test_uc.py
if [ $? -eq 0 ]
then
  curl -o .badges/unittest.svg https://img.shields.io/badge/unittest-passing-green.svg?longCache=true&style=flat
else
  curl -o .badges/unittest.svg https://img.shields.io/badge/unittest-failing-red.svg?longCache=true&style=flat
fi

# Run static type checking and generate SVG
python3 -m mypy uc.py
if [ $? -eq 0 ]
then
  curl -o .badges/mypy.svg https://img.shields.io/badge/mypy-passing-green.svg?longCache=true&style=flat
else
  curl -o .badges/mypy.svg https://img.shields.io/badge/mypy-failing-red.svg?longCache=true&style=flat
fi

# Lint and get just the score
PYLINT_SCORE=$(python3 .pylint-score.py)
if [ "$PYLINT_SCORE" == "10.0" ]
then
	curl -o .badges/pylint.svg https://img.shields.io/badge/PyLint_score-$PYLINT_SCORE-green.svg?longCache=true&style=flat
else
	curl -o .badges/pylint.svg https://img.shields.io/badge/PyLint_score-$PYLINT_SCORE-red.svg?longCache=true&style=flat
fi
