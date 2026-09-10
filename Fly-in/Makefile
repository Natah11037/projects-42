.SILENT:

PYTHON := .venv/bin/python
MAP ?= assets/maps/easy/01_linear_path.txt

.PHONY: install run debug clean lint lint-strict

install:
	@command -v uv >/dev/null 2>&1 || { echo "uv is not installed. Run 'make install' after installing uv."; exit 1; }
	@uv sync -q
	@test -x $(PYTHON) || { echo "Virtual environment not found. Run 'make install' again."; exit 1; }

run:
	@test -x $(PYTHON) || { echo "Virtual environment not found. Run 'make install' first."; exit 1; }
	@MAP="$(MAP)" $(PYTHON) -m source.main

debug:
	@test -x $(PYTHON) || { echo "Virtual environment not found. Run 'make install' first."; exit 1; }
	@MAP="$(MAP)" $(PYTHON) -m pdb -m source.main

clean:
	@find . -type d -name __pycache__ -prune -exec rm -rf {} +
	@rm -rf .mypy_cache .pytest_cache

lint:
	@$(PYTHON) -m flake8 source --exclude=.venv
	@$(PYTHON) -m mypy source --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@$(PYTHON) -m flake8 source --exclude=.venv
	@$(PYTHON) -m mypy source --strict
