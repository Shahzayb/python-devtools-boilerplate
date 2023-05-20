POETRY = poetry

all: install

.PHONY: install
install:
	$(POETRY) install

.PHONY: test
test:
	$(POETRY) run pytest --cov=src --cov-report=term-missing -n auto
ifeq ($(OS),Windows_NT)
	@echo "Cleaning up .coverage file (Windows)"
	del /F /Q .coverage
else
	@echo "Cleaning up .coverage file (Unix)"
	rm -f .coverage
endif

.PHONY: lint
lint:
	$(POETRY) run flake8 ./src

.PHONY: format
format:
	$(POETRY) run black ./src

.PHONY: mypy
mypy: 
	$(POETRY) run mypy

.PHONY: watch
watch:
	$(POETRY) run python -m src.watch
