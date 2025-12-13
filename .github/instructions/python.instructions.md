---
applyTo: "**/*.py"
---
# Python Instructions for This Repository

## Running the Application
- use `uv run` to run the application (we use uv for env management and better cross-platform compatibility
)
## Style and Formatting
- All Python code must strictly follow the PEP 8 style guide.
- Use the `ruff` code formatter for consistent formatting. Set the maximum line length to 88 characters.

---

## Modularity and Code Structure
- **Follow the Single Responsibility Principle (SRP).** Each function and class should do one thing well.
- **Keep functions small and focused.** If a function is too long, break it into smaller helper functions.

---

## Code Quality and Best Practices
- **Use `pathlib` for all file system path manipulations.**
- Use context managers (`with` statement) for file/resource handling.
- Prefer f-strings for string formatting.
- Avoid mutable default arguments.

---

## Error Handling and Logging
- Use specific exception types (e.g., `ValueError`).
- **Use the standard `logging` module with `colorlog` for all output.** Do not use `print()`.

---

## Design Patterns & Performance
- **Apply common design patterns** (Factory, Observer, etc.) where appropriate and add a comment explaining your choice.
- **Write efficient, "Pythonic" code.** Use comprehensions and generators, and be mindful of algorithmic complexity.

---

## Testing & Security
- **Use the `pytest` framework** for all tests.
- **Always sanitize user input** and load secrets from environment variables.

---

## Dependency Management
- **Use Poetry** to manage dependencies. Assume a `pyproject.toml` file exists for this purpose.