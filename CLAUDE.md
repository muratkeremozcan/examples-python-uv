# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python learning repository using uv for dependency management. It contains progressive Python examples from basic concepts to advanced OOP patterns, data visualization, and testing practices.

## Development Commands

### Environment Management

```bash
# Required setup
brew install uv
uv sync --all-extras

# Optional: direnv for auto-activation (shorter commands)
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc
echo 'source .venv/bin/activate' > .envrc
echo 'export PATH="$PWD/.venv/bin:$PATH"' >> .envrc
direnv allow .
```

### Code Quality

```bash
# Format code
uv run black .              # Code formatting (88 char line length)
uv run isort .              # Import organization

# Lint code
uv run flake8               # Linting (ignores E203, W503, E501, E266, F811, F841, F401, E402)

# Check syntax
find . -name "*.py" -type f -exec uv run python -m py_compile {} +

# Combined formatting and linting (recommended)
uv run black . && uv run isort . && uv run flake8
make validate                    # Same as above using Makefile

# Create shell alias for convenience (add to ~/.zshrc or ~/.bashrc)
# alias uvvalidate="uv run black . && uv run isort . && uv run flake8"
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest 08.testing/test_01_basic.py

# Run specific test by name
uv run pytest -k "test_name"

# Run with coverage
uv run pytest --cov
```

### Package Management

```bash
# Add regular dependency
uv add package_name

# Add dev dependency
uv add --optional dev package_name

# Show installed packages
uv tree

# Sync dependencies
uv sync --all-extras
```

## Architecture & Code Organization

### Directory Structure

- `01.intro/` - Basic Python syntax, data types, control flow
- `02.intermediate/` - Functions, modules, error handling, pandas basics
- `03.data-visualization/` - Iterators, generators, CSV processing, list comprehensions
- `04.data-types/` - Deep dive into Python collections and numeric types
- `05.functions/` - Advanced function concepts, decorators, context managers
- `06.efficient-python-code/` - Performance optimization, profiling, numpy
- `07.swe-principles/` - Package structure, docstrings, doctest
- `08.testing/` - pytest and unittest examples with fixtures and performance tests
- `09.OOP/` - Object-oriented programming patterns and principles
- `10.toolbox/` - Date/time handling, pandas datetime operations
- `11.APIs/` - HTTP requests and API interaction

### Key Dependencies

- **Core**: `numpy`, `pandas`, `matplotlib`, `seaborn` for data analysis/visualization
- **Testing**: `pytest`, `pytest-benchmark` for testing and performance measurement
- **Development**: `black`, `flake8`, `isort`, `autopep8` for code quality
- **Profiling**: `line-profiler`, `memory-profiler` for performance analysis
- **Utilities**: `requests`, `deepdiff`, `deepmerge` for various operations

### Code Style Configuration

- **Black**: 88 character line length, Python 3.12 target
- **isort**: Black-compatible profile with trailing commas
- **flake8**: Relaxed line length (200 chars), ignores common Black conflicts

### Sample Projects

- `09.OOP/sample-calculator/` - Financial calculator with inheritance and class structure
- `09.OOP/sample-inventory-management/` - Complete inventory system with products and orders
- `09.OOP/sample-project-smartphone/` - Data visualization project with testing structure

### Testing Patterns

- Unit tests in `08.testing/` demonstrate pytest fixtures, autouse, and performance testing
- Integration tests show data pipeline testing with both unittest and pytest
- Sample projects include comprehensive test suites with proper separation of unit/integration tests

## Running Examples

Most Python files can be executed directly:

```bash
python 01.intro/01-math-operations.py
python 09.OOP/sample-calculator/main.py
```

For modules with dependencies, ensure the virtual environment is activated or use:

```bash
uv run python path/to/script.py
```
