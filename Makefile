.PHONY: install install-dev format create-venv

install:
	@pip install -e .

install-dev:
	@pip install -e .[dev]

format:
	@isort lmgdataset/
	@black lmgdataset/
	@flake8 lmgdataset/

create-venv:
	@python3.10 -m venv venv
	@. venv/bin/activate
