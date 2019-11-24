# Makefile

Usual tasks during development can be solved using the
[Makefile](../../../references/index.html#makefile).

The basic Makefile created in your project created with `create_service`-util
of [fastapi-serviceutils](../../../references/index.html#fastapi-serviceutils)
serves the following commands:


## make help
Show available make commands for the project.


## make init
Initialize project.
To be run after `create_service` to create the pyenv for the project.


## make check
Run linters and checkers using
[pre-commit](../../../references/index.html#pre-commit).


## make clean
Cleans the working directory.
Deletes usual cache- and temp-files.


## make docker
Create the poetry.lock for the main-env and create docker-image for project.
Tag of the docker-image is extracted from the version defined in
`pyproject.toml`.


## make docs
Create [MkDocs](../../../references/index.html#mkdocs) documentation for the
project.


## make finalize
Finalize the main env and create the poetry.lock.


## make info
Show info about current project like used python-version and used
dependencies.


## make tests
Run tests defined for the project using
[Pytest](../../../references/index.html#pytest).


## make update
Update environments based on `pyproject.toml` definitions and run
[pre-commit](../../../references/index.html#pre-commit).
