# Pre-commit

To ensure clean-coding during developing at this service we use
[pre-commit](../../../references/index.html#pre-commit)
with a couple of linters and checkers.

Because we want to have PEP8-oriented code we use
[Black](../../../references/index.html#black),
[Flake8](../../../references/index.html#flake8),
[pydocstyle](../../../references/index.html#pydocstyle) and
[codespell](../../../references/index.html#codespell) in combination with some
checkers for correctness of project-relevant files like the `pyproject.toml`,
correct naming of test-files, etc.

To run all pre-commit-hooks manually run the
[Make](../../../references/index.html#make) command:
```bash
    make check
```
