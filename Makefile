.PHONY: check lint install format format-check sync validate
# type-check is disabled as per user preference

lint:
	uv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

check:
	find . -name "*.py" -type f -exec uv run python -m py_compile {} +

# Type checking disabled - uncomment if needed later
# type-check:
#	uv run mypy --config-file=mypy.ini .

install:
	uv sync --all-extras

sync:
	uv sync --all-extras

format:
	uv run black .
	uv run isort .

format-check:
	uv run black --check .
	uv run isort --check-only .

validate:
	uv run black .
	uv run isort .
	uv run flake8

all: install lint check format-check
# type-check removed from 'all' command
