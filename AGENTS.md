# Repository Guidelines

## Project Structure & Modules
- Numbered lesson folders (`01.intro` … `13.Reshaping-data-with-pandas`) hold topic-specific scripts/notebooks; add new material to the matching topic.
- Testing examples live in `08.testing` (pytest + unittest demos) and in sample app trees under `09.OOP/sample-*`.
- Shared config lives in `pyproject.toml`, `uv.lock`, `Makefile`, and `README.md` (setup + workflow notes).

## Setup, Build, Test Commands
- `uv sync --all-extras` — install deps and create `.venv/` (Python 3.12 target).
- `uv run python <path/to/script.py>` — run any lesson script; skip `uv run` only if `.venv` is already activated via direnv.
- `uv run pytest` or `uv run pytest 08.testing/test_01_basic.py` — run all or targeted tests; add `--cov` for quick coverage snapshots.
- `make validate` — format (black + isort) then flake8; `make format` to auto-format only.
- `make lint` — flake8 error scan; `make check` — bytecode compilation guard for all `.py` files.

## Coding Style & Naming
- Formatting: black (line length 88); imports: isort with black profile; lint: flake8 (max line length 200, common formatting ignores).
- Use 4-space indentation; snake_case for modules/functions/variables, PascalCase for classes, UPPER_SNAKE_CASE for constants.
- Keep functions small and focused; add type hints where they clarify intent; prefer pure functions inside lesson modules.

## Testing Guidelines
- Default to pytest for new coverage; follow existing unittest style only where already present (e.g., `08.testing/test_09_unittest.py`).
- Name tests by behavior (`test_<action>_<expectation>`); place them beside the related topic folder or under the sample app’s `tests/` tree.
- Use fixtures instead of ad hoc setup; keep benchmark/perf tests opt-in and isolated.
- Run `uv run pytest -q` before PRs; include `--cov` when touching logic-heavy sections.

## Commit & PR Guidelines
- Commit style matches history: conventional commits (`feat: add pandas reshape demo`, `fix: guard division by zero`); keep changes atomic.
- PRs should include a concise summary, commands/tests run, screenshots/plots when visuals change, and linked issue or lesson reference if relevant.
- Ensure format/lint/tests pass and `uv.lock` stays in sync when deps change; avoid committing `.venv` or local data files.

## Security & Configuration Tips
- Never commit secrets or tokens; rely on local env vars or `.envrc` (ignored by git).
- Keep datasets lightweight; store larger samples outside the repo and document the path.
- If tooling drifts, `uv cache clean` then `rm -rf .venv && uv sync --all-extras` resets the environment cleanly.
