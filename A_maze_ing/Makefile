.SILENT:

install:
# Checking if uv is installed, if not telling the user to install it before doing anything else. Then,
# using uv sync to configure the environment in silence. Then,
# checking if the venv is correctly set up
	@command -v uv >/dev/null 2>&1 || { echo "uv is not installed. Please consider installing uv before doing anything else."; exit 1; }
	@uv sync -q || { echo "uv sync failed"; exit 1; }
	@command -v .venv/bin/python >/dev/null 2>&1 || { echo "Virtual environment not found."; exit 1; }

run:
	@if [ ! -f .venv/bin/python ]; then echo "\nVirtual environment not found. Run 'make install' first.\n"; else .venv/bin/python a_maze_ing.py config.txt; fi

debug:
	@.venv/bin/python -m pdb a_maze_ing.py || true

clean:
	@rm -rf */__pycache__ .mypy_cache configuration/__pycache__ .pytest_cache
	@rm -rf */*/__pycache__ .mypy_cache configuration/__pycache__ .pytest_cache

lint:
	@.venv/bin/python -m flake8 . --exclude=.venv
	@.venv/bin/python -m mypy . --exclude .venv --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@.venv/bin/python -m flake8 . --exclude=.venv
	@.venv/bin/python -m mypy . --exclude .venv --strict
