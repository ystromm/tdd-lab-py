export PYTHON_VERSION = python3.7

venv:
	virtualenv venv --python=$$PYTHON_VERSION

# Dev

venv/requirements-standalone-dev.txt: requirements-standalone-dev.txt requirements.txt
	(. venv/bin/activate && \
	pip3 install -r requirements-standalone-dev.txt && \
	pip3 install \
	-r requirements.txt && \
	cp requirements-standalone-dev.txt venv/)

.PHONY: test
test: venv venv/requirements-standalone-dev.txt
	@ . venv/bin/activate && flake8  src test --exclude '#*,~*,.#*'
	@ . venv/bin/activate && nosetests

# Cleaning

.PHONY: clean
clean:
	rm -rf dist
	rm -rf venv
	find . -name "*.pyc" -delete
