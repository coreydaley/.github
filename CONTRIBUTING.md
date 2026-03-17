# Contributing

Thanks for your interest in contributing! These guidelines apply to all repositories under [@coreydaley](https://github.com/coreydaley) that don't define their own `CONTRIBUTING.md`.

## Getting started

1. **Search existing issues** before opening a new one to avoid duplicates.
2. **Open an issue first** for significant changes so we can discuss the approach before you invest time writing code.
3. **Fork the repository** and create a branch from `main`.

## Pull requests

- Keep PRs focused — one feature or fix per PR.
- Write clear commit messages using [Conventional Commits](https://www.conventionalcommits.org/):
  ```
  feat(scope): add support for X
  fix(scope): correct Y when Z
  ```
- Update documentation and tests where applicable.
- Ensure CI checks pass before requesting review.

## Code style

- Follow the conventions already present in the codebase.
- Avoid over-engineering; implement only what is needed.
- Do not add comments unless the logic is non-obvious.

## Reporting bugs

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) and include:
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, runtime versions, etc.)

## Security vulnerabilities

Please do **not** open a public issue for security vulnerabilities. See [SECURITY.md](SECURITY.md) for the responsible disclosure process.

## Code of conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it.
