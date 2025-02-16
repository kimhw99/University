# Phony targets
.PHONY: all install test tests 

# Detect OS
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell uname -s)
endif

# Set path separator
ifeq ($(detected_OS),Windows)
	PATHSEP := ;
else
	PATHSEP := :
endif

# Set PYTHONPATH
export PYTHONPATH := .$(PATHSEP)$(PYTHONPATH)

# Default target
all: test

# Install dependencies
install:
	pip install -e .
	pip install pytest

# Run all tests
test: tests

tests:
	pytest -s --color=yes

# Run linear regression tests
lr:
	pytest -s --color=yes ./tests/test_linear_regression.py

# Run feature tests
features:
	pytest -s --color=yes ./tests/test_features.py
