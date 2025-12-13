---
applyTo: "terminal"
---
# Instructions for Terminal Commands

- **Operating System**: I am using windows with wsl zsh. Please provide ubuntu commands (e.g., use `rm`, `ls`, `mkdir`).

---

## Safety and Confirmation
- **Destructive Commands**: For any potentially destructive command like `rm` or `mv`, always include the `-i` flag to prompt before execution. For Git commands like `git reset` or `git push --force`, add a comment like `# DANGER: This is a destructive command. Please double-check your changes.`
- **Piping to Shell**: Never suggest piping `curl` or `Invoke-WebRequest` directly into a shell. Suggest downloading the script first, then running it after user inspection.

---

## Git Workflow
- **Branch Naming**: Follow the `type/short-description` format when suggesting `git checkout -b`. (e.g., `git checkout -b feat/new-login-page`).
- **Commit Messages**: When suggesting `git commit -m`, use the Conventional Commits format (`feat: ...`, `fix: ...`).

---

## Project-Specific Commands

- **Dependency Management**: Use `uv sync` to install dependencies from `pyproject.toml`.
- **Running the Project**: Use `uv run main.py` (or `uv run -m your_project_name.main` for modules).
- **Running Tests**: Use `uv run pytest` to run tests.