# Python Environment with uv

## Setup

### Required (Minimal)

```bash
# 1. Install uv (handles Python + virtual environments automatically)
brew install uv

# 2. Install dependencies in project directory
uv sync --all-extras
```

That's it! uv automatically:

- Installs the correct Python version (3.12+)
- Creates a virtual environment in `.venv/`
- Installs all dependencies

### Optional (Convenience)

For shorter commands without `uv run` prefix:

```bash
# Install direnv for auto-activation
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && source ~/.zshrc

# Setup auto-activation in project directory
echo 'source .venv/bin/activate' > .envrc               # Auto-activates when entering directory
echo 'export PATH="$PWD/.venv/bin:$PATH"' >> .envrc     # Run tools directly without uv run
direnv allow .                                          # Approve the script
```

**With direnv:** `python script.py`, `black .`, `pytest`  
**Without direnv:** `uv run python script.py`, `uv run black .`, `uv run pytest`

## Day-to-day Workflow

### Using Tools (after auto-activation or with uv run)

```bash
python script.py
black .       # Format code (like prettier)
isort .       # Organize imports
flake8        # Lint code (like eslint)

# Or use uv run for explicit execution
uv run python script.py
uv run black .
uv run isort .
uv run flake8

# Combined formatting and linting (recommended)
uv run black . && uv run isort . && uv run flake8
make validate                    # Same as above using Makefile

# Create shell alias for convenience (add to ~/.zshrc or ~/.bashrc)
# alias uvvalidate="uv run black . && uv run isort . && uv run flake8"

# Run tests
uv run pytest        # Run all tests
uv run pytest -v     # Verbose output
uv run pytest -k "test_name"  # Run specific test
uv run pytest --cov  # Run with coverage report
uv run pytest 08.testing/test_01_basic.py
```

### Managing Packages

```bash
# Add packages
uv add requests              # Regular dependency (like npm install)
uv add --optional dev pytest         # Dev dependency (like npm install --save-dev)

# Remove packages
uv remove requests

# Update packages
uv sync --upgrade

# Show packages
uv tree                      # Show dependency tree
```

## Troubleshooting

```bash
# If things break, try these:
uv cache clean               # Clear cache
rm -rf .venv && uv sync --all-extras  # Reset environment
```

## Why uv over Poetry?

| Feature                   | Poetry                                                         | uv                                                              |
| ------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| **Speed**                 | Moderate (Python-based)                                       | **Extremely fast (Rust-based)**                                |
| **Dependency Resolution** | Good resolver                                                  | **Lightning-fast resolver**                                     |
| **Installation**          | `poetry install`                                               | `uv sync` (faster, cleaner syntax)                             |
| **Package Management**    | `poetry add/remove`                                            | `uv add/remove` (simpler, faster)                              |
| **Configuration**         | `pyproject.toml` + `poetry.lock`                              | **Standard `pyproject.toml` + `uv.lock`**                      |
| **Python Version Mgmt**  | External (pyenv, etc.)                                         | **Built-in Python version management**                         |
| **Virtual Environments** | Creates `.venv`                                                | **Automatic venv management**                                   |
| **Standards Compliance** | Poetry-specific format                                         | **Pure PEP 517/518/621 compliant**                             |
| **Tool Integration**      | `poetry run <command>`                                         | `uv run <command>` (faster execution)                          |

## Three-Way Comparison: Pip vs Poetry vs uv

| Feature                 | Pip                                                          | Poetry                                                       | uv                                                     |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| **Speed**               | Moderate                                                     | Moderate (Python-based)                                     | **10-100x faster (Rust-based)**                       |
| **Config File**         | `requirements.txt` (flat list)                               | `pyproject.toml` + Poetry-specific sections                 | **Standard `pyproject.toml` (PEP 621)**               |
| **Lock File**           | None built-in (requires `pip-tools` for `requirements.lock`) | `poetry.lock` (automatically generated)                     | **`uv.lock` (faster generation)**                     |
| **Python Management**   | External (pyenv, python.org, etc.)                          | External (pyenv, etc.)                                       | **Built-in with `uv python`**                         |
| **Virtual Environments**| Manual `python -m venv`                                      | `poetry install` (creates `.venv`)                          | **Automatic with `uv sync`**                          |
| **Dependency Resolution**| Basic (can have conflicts)                                   | Good resolver                                                | **Lightning-fast advanced resolver**                  |
| **Dev Dependencies**    | Separate file or mixed with production deps                  | `[tool.poetry.group.dev]`                                   | **`[project.optional-dependencies]` (standard)**      |
| **Installation**        | `pip install -r requirements.txt`                           | `poetry install`                                             | **`uv sync` (much faster)**                           |
| **Package Building**    | Manual with setuptools/build                                | `poetry build`                                               | **`uv build` (integrated)**                           |
| **Standards Compliance**| Basic                                                        | Poetry-specific extensions                                   | **Full PEP 517/518/621 compliance**                   |
| **Tool Integration**    | Direct execution (after activation)                         | `poetry run <command>`                                       | **`uv run <command>` (faster execution)**             |
| **Learning Curve**      | Moderate (multiple tools needed)                             | Moderate (Poetry-specific concepts)                          | **Easy (familiar commands, faster)**                  |
| **Ecosystem**           | Mature, universal                                            | Popular, growing                                             | **Fast-growing, modern**                               |
