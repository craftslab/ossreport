#!/bin/bash

chmod 644 .gitignore .pre-commit-config.yml .travis.yml
chmod 644 Dockerfile LICENSE Makefile MANIFEST.in README.md requirements.txt setup.cfg
chmod 644 report.py setup.py

find ossreport tests -name "*.json" -exec chmod 644 {} \;
find ossreport tests -name "*.py" -exec chmod 644 {} \;
find ossreport tests -name "*.yml" -exec chmod 644 {} \;
find . -name "*.pyc" ! -path "*.venv*" -exec rm -rf {} \;
find . -name "*.sh" ! -path "*.venv*" -exec chmod 755 {} \;
find . -name "__pycache__" ! -path "*.venv*" -exec rm -rf {} \;
