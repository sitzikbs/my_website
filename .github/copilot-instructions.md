# General Instructions for This Repository

## Core Principles & Code Health
- **Clarity is Key**: Write code that is simple, readable, and self-explanatory.
- **DRY (Don't Repeat Yourself)**: Avoid duplicating code. Encapsulate and reuse logic whenever possible.
- **No Hardcoded Secrets**: Never commit API keys, passwords, or other sensitive data. Load them from environment variables.
- **Remove Dead Code**: Be proactive about deleting commented-out code, unused variables, and unreachable logic. Keep the codebase clean.

---

## Project Configuration
- **Environment Variables**: When new environment variables are needed, also add them to a `.env.example` file with placeholder values. This file should be committed to the repo.
- **Git Ignore**: When adding new tools or frameworks, update the `.gitignore` file with their standard ignore patterns (e.g., add `node_modules/`, `__pycache__/`, `.venv/`).
- **pythin environment**: use `uv` to run python commands for better compatibility across systems.
---

## Documentation
- **Inline Comments**: For any logic that is complex or non-obvious, add a brief, clear comment explaining the "why," not just the "what."
- **README Updates**: If you add a new feature that requires setup, new environment variables, or a new library, add the necessary documentation to the `README.md` file.

---

## Git Workflow
- **gh CLI**: Use the GitHub CLI (`gh`) for managing issues and pull requests from the command line.
- **Branch Naming**: When suggesting git commands, name new branches using the `type/short-description` format (e.g., `feat/user-auth`, `fix/api-bug`).
- **Commit Messages**: Follow the Conventional Commits specification. [Image of Conventional Commits examples chart] Start with a type (`feat`, `fix`, `docs`, `refactor`, `test`) and link to related issues if applicable.
- **Example Commit**: `feat: add user authentication endpoint (closes #42)`
- **Opening Issues**: When creating issues, provide a clear title, detailed description, steps to reproduce (if applicable), and any relevant screenshots or logs.
- **Working on Issues**: When working on an issue, first pull the latest main, then create a new branch with an informative name. Reference it in your commit messages and pull requests using `#issue-number` to create a link.
- **Closing Issues** : When your code resolves an issue, include `closes #issue-number` in your commit message to automatically close it upon merging and open a PR.
- **Pull Requests**: When opening a pull request, provide a clear title and description of the changes made. Reference any related issues using `#issue-number`. Ensure all tests pass before requesting a review.

---

## Naming Conventions
- **General Files**: For non-Python files (like JS, CSS, HTML, or Markdown files), use `kebab-case` for naming (e.g., `user-profile.js`, `main-styles.css`).

# Temporary tests
- If you need to do a test to verify functionality, place the file in a `tests/` subdirectory.
- Name the test file descriptively, indicating the functionality being tested (e.g., `test_user_auth.py`).
- If the test is temporary for debugging purposes, clearly mark it as such and remove it once it's no longer needed.
- Include a brief description of the test's purpose and any relevant context within the test file itself (at the top). Explicitly indicate if it is temporary or a permanent test.
