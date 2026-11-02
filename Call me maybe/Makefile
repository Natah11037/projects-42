.PHONY: install run debug clean lint lint-strict
.SILENT:

install:
	uv sync

run:
	uv run python -m src $(ARGS)

debug:
	uv run python -m pdb -m src

clean:
	find . -type d \( -name __pycache__ -o -name .mypy_cache -o -name .pytest_cache \) -prune -exec rm -rf {} +

lint:
	uv run --with flake8 --with mypy flake8 .
	uv run --with flake8 --with mypy mypy src --follow-imports=silent --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run --with flake8 --with mypy flake8 .
	uv run --with flake8 --with mypy mypy src --follow-imports=silent --strict
