# Pre-commit

To ensure clean-coding during developing at this service we use pre-commit
with a couple of linters and checkers.

Because we want to have PEP8-oriented code we use `Black`, `Flake8`,
`pydocstyle` and `codespell` in combination with some checkers for correctness
of project-relevant files like the pyproject-toml, correct naming of
test-files, etc.

To run all pre-commit-hooks manually run:
```bash
    make check
```
