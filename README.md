# NewCoolPublicProject

A Python 3.12 project using uv and ruff that computes the square root of a given number.

## Requirements

- Python 3.12
- uv (Python package manager)
- ruff (Python linter)

## Installation

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Install project dependencies:
```bash
uv sync
```

## Usage

Run the square root calculator:
```bash
uv run python main.py <number>
```

Examples:
```bash
uv run python main.py 16
# Output: The square root of 16.0 is 4.0

uv run python main.py 25
# Output: The square root of 25.0 is 5.0

uv run python main.py 2
# Output: The square root of 2.0 is 1.4142135623730951
```

## Development

### Linting

Run ruff to check code quality:
```bash
uv run ruff check .
```

Format code with ruff:
```bash
uv run ruff format .
```

## Project Structure

- `main.py` - Main script with square root computation
- `pyproject.toml` - Project configuration and dependencies
- `.python-version` - Python version specification