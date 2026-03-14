.PHONY: help venv install run check clean

VENV ?= .venv
PYTHON ?= python3
POST ?=
MODEL ?= llama3.1
VENV_PYTHON := $(VENV)/bin/python

help:
	@printf '%s\n' \
		'make venv                 Create the local virtual environment' \
		'make install              Install Python dependencies into the virtual environment' \
		'make run POST=<slug>      Run the generator locally for a post slug' \
		'make run POST=<slug> MODEL=<model>  Override the Ollama model' \
		'make check                Syntax-check the Python source tree' \
		'make clean                Remove the virtual environment'

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

venv:
	@if [ ! -x "$(VENV_PYTHON)" ]; then \
		$(PYTHON) -m venv $(VENV); \
	fi
	@$(VENV_PYTHON) -m ensurepip --upgrade >/dev/null
	@$(VENV_PYTHON) -m pip --version >/dev/null

install: venv
	$(VENV_PYTHON) -m pip install -r requirements.txt

run: install
ifndef POST
	$(error POST is required, e.g. make run POST=my-post)
endif
	$(VENV_PYTHON) src/__main__.py $(POST) --model $(MODEL)

check: install
	$(VENV_PYTHON) -m py_compile $(shell rg --files src -g '*.py')

clean:
	rm -rf $(VENV)
