.DEFAULT_GOAL := help
PYTHON ?= python3
VENV   := .venv
BIN    := $(VENV)/bin

.PHONY: help setup lint format repo-check notebooks template-test check mdlint docs clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

setup: ## Create .venv, install tools and enable the pre-commit hooks
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements-dev.txt
	$(BIN)/pre-commit install
	@echo "Done. Activate with: source $(VENV)/bin/activate"

lint: ## Lint and check formatting (Ruff)
	$(BIN)/ruff check .
	$(BIN)/ruff format --check .

format: ## Auto-fix lint issues, format code and clear notebook outputs
	$(BIN)/ruff check --fix .
	$(BIN)/ruff format .
	$(BIN)/nbstripout weekly-sessions/*/*.ipynb

repo-check: ## Check links, structure, member profiles and clean notebooks
	$(BIN)/python scripts/check_repo.py

notebooks: ## Run every teaching notebook top to bottom
	$(BIN)/pytest --nbmake weekly-sessions

template-test: ## Test the starter project template
	cd projects/_template && ../../$(BIN)/pytest

check: lint repo-check notebooks template-test ## Run everything CI runs (except markdown lint)

mdlint: ## Lint Markdown (needs Node.js)
	npx --yes markdownlint-cli2

docs: ## Preview the docsify site at http://localhost:3000
	$(BIN)/python -m http.server 3000

clean: ## Remove the virtual environment and tool caches
	rm -rf $(VENV) .pytest_cache .ruff_cache projects/_template/.pytest_cache projects/_template/reports
	find . -name ".ipynb_checkpoints" -type d -prune -exec rm -rf {} +
