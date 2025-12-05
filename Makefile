.PHONY: dev test

VENV?=
PIP?=pip
PYTHON?=python

install:
$(PIP) install -r requirements.txt

install-test:
$(PIP) install -r requirements.txt -r test-requirements.txt

dev: install
$(PYTHON) -m swagger_server

test: install-test
pytest
