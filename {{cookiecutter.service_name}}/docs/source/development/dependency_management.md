# Dependency management


## Basics

We use Poetry_ including the dependency definition inside the
`pyproject.toml` and `python-venv` for environment management.
For a wrapper around these tools we use Dephell_ and `make` for easier
workflow.

**dependency management relevant files:**

```bash
    <SERVICENAME>
    ├── ...
    ├── poetry.lock
    ├── pyproject.toml
    ├── .python-version
    └── ...
```

* `pyproject.toml`: stores what dependencies are required in which versions.
  Required by Dephell_ and Poetry_.
* `poetry.lock`: locked definition of installed packages and their versions
  of currently used environment.
  Created by Poetry_ using `make init`, `make update`, `make tests` or
  `make finalize`.
* `.python-version`: the version of the python-interpreter used for this
  project.
  Created by `pyenv` using `make init`, required by Poetry_ and Dephell_.


## Updating dependencies

!!! attention

    To update the dependencies of your project ensure the projects pyenv
    environment to be activated.
    
    To activate it use:
    ```
        poetry shell
    ```

If additional dependencies are required for the service, these are added into
the `pyproject.toml` file.
After each change in dependencies defined at `pyproject.toml` run the
following to ensure the environment-definition and lock-file are up to date:
```bash
    make update
```
This updates the dependencies in the current environment using poetry.
