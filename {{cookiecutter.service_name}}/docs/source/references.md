# References

Collection of references, blogs, documentation pages for used packages, tools.


## Black

Code formatter for python.
Used during development of this service inside [pre-commit](#pre-commit).
Is configured inside the `pyproject.toml`.

As described in official documentation:
> Blackened code looks the same regardless of the project you're reading.
> Formatting becomes transparent after a while and you can focus on the
> content instead.
>
> Black makes code review faster by producing the smallest diffs possible.

Documentation and useful additional resources:

* [black](https://black.readthedocs.io/en/stable/)


## Codespell

Check misspellings in code.
Used during development of this service inside [pre-commit](#pre-commit).
Is configured inside the `.pre-commit-config.yml`.

Documentation and useful additional resources:

* [Codespell](https://github.com/codespell-project/codespell)


## Cookiecutter

Cookiecutter creates projects from project templates using jinja2.

Cookiecutter is used inside `create_service` of fastapi-serviceutils to create
new service using template as defined at
[fastapi_serviceutils_template](https://github.com/skallfass/fastapi_serviceutils_template).

Documentation and useful additional resources:

* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)


## Databases

Simple asyncio support for a range of databases.
Allows to make queries using [SQLAlchemy](#sqlalchemy).

As recommended by fastapi-documentation, fastapi-serviceutils services use the
package databases to interact with databases.

Documentation and useful additional resources:

* [Databases](https://www.encode.io/databases/)


## Dephell

Dephell is a tool for project management for Python.

In our workflow we use it to convert the dependencies of a project as defined
inside the `pyproject.toml` to a `requirements.txt` as it is used inside the
`Dockerfile` to convert a service to a docker-image.

Usage is configured inside the `pyproject.toml`.

It is automatically used inside `make docker` and `make finalize` (see
[makefile](../development/helpers/makefile)).

Documentation and useful additional resources:

* [Dephell](https://dephell.org/docs/)


## Docker

Used to containerize the service in deployment.

As described in official docker-documentation:
> Docker is an open platform for developing, shipping, and running
> applications.
> Docker enables you to separate your applications from your infrastructure
> so you can deliver software quickly.
> With Docker, you can manage your infrastructure in the same ways you manage
> your applications.
> By taking advantage of Docker’s methodologies for shipping, testing, and
> deploying code quickly, you can significantly reduce the delay between
> writing code and running it in production.

Documentation and useful additional resources:

* [docker overview](https://docs.docker.com/engine/docker-overview/)
* [Dockerfile](https://docs.docker.com/engine/reference/builder/)
* [docker cli](https://docs.docker.com/engine/reference/run/)


## Docker-compose

Used to wrap the docker-command at deployment of the service and easier usage
of port-mappings and environment-variable definition.

As described in the official docker-compose-documentation:
> Compose is a tool for defining and running multi-container Docker
> applications.
> With Compose, you use a YAML file to configure your application’s services.
> Then, with a single command, you create and start all the services from your
> configuration.
> ...
>
> Compose works in all environments: production, staging, development,
> testing, as well as CI workflows.
> ...
>
> Using Compose is basically a three-step process:
> 
> * Define your app’s environment with a Dockerfile so it can be reproduced
>   anywhere.
> * Define the services that make up your app in docker-compose.yml so they can
>   be run together in an isolated environment.
> * Run docker-compose up and Compose starts and runs your entire app.

Documentation and useful additional resources:

* [docker-compose overview](https://docs.docker.com/compose/)
* [docker-compose.yml](https://docs.docker.com/compose/compose-file/)
* [docker-compose cli](https://docs.docker.com/compose/reference/overview/)


## Environment variable

As described at wikipedia:
> An environment variable is a dynamic-named value that can affect the way
> running processes will behave on a computer.

Inside the service `Environment variables` are used to be able to overwrite
service-settings from the `config.yml`.

For details about how to configure the service, see
[configuration](../configuration).

Documentation and useful additional resources:

* [Environment variable](https://en.wikipedia.org/wiki/Environment_variable)


## FastAPI

High-performance web framework for building APIs with python 3.6+.
Based on open standard for APIs ([OpenAPI](#openapi)).
For the definition of the input- and output-models of endpoints
[Pydantic][#pydantic] is used.

This service is mainly based on this framework!
All additional packages are used around this package.

Documentation and useful additional resources:

* [FastAPI](https://fastapi.tiangolo.com/)


## fastapi-serviceutils

Additional utils and functions for easier creation and usage of
[FastAPI](#fastapi).

Documentation and useful additional resources:

* [fastapi-serviceutils](https://fastapi-serviceutils.readthedocs.io/en/latest/)


## Flake8

Modular source code checker for pep8, pyflakes and co.
Used during development of this service inside [pre-commit](#pre-commit).
Is configured inside the `setup.cfg`.

Documentation and useful additional resources:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pep8](https://www.python.org/dev/peps/pep-0008/)
* [pep8 the style guide for python code](https://pep8.org/)


## Flake8-bugbear

A plugin for [Flake8](#flake8) finding likely bugs and design problems in your program.
Contains warnings that don't belong in pyflakes and [pycodestyle](#pydocstyle).

Used in [pre-Commit](#pre-commit) of the service.
Is configured inside the `setup.cfg`.

Documentation and useful additional resources:

* [Documentation](https://github.com/PyCQA/flake8-bugbear)


## Git

Git is a free and open source distributed version control system.

The service is versioned using git.
For additional information about the git-workflow used in this service see
[git-workflow](../development/git_workflow).

Documentation and useful additional resources:

* [git](https://git-scm.com/doc)
* [stable mainline branching model for git](http://www.bitsnbites.eu/a-stable-mainline-branching-model-for-git/)


## git-extras

Contain some additional git commands for easier git workflow.

Documentation and useful additional resources:

* [git-extras](https://github.com/tj/git-extras)
* [git-extras commands](https://github.com/tj/git-extras/blob/master/Commands.md)


## Loguru

For better traceback in log-files and usage of request-id as context inside
log-entries, the default logging of fastapi is extended by usage of loguru
inside services based on fastapi-serviceutils.

Documentation and useful additional resources:

* [Loguru](https://loguru.readthedocs.io/en/stable/index.html)


## Make

To wrap common tasks during development of the service, commands are wrapped
inside a makefile.

Is configured inside `Makefile`.
For available make-commands during development of the service see
[makefile](../development/helpers/makefile).

Documentation and useful additional resources:

* [Make](https://www.gnu.org/software/make/manual/make.html)


## Markdown

Description from [commonmark.org](https://commonmark.org/help/):
> Markdown is a simple way to format text that looks great on any device.
> It doesn’t do anything fancy like change the font size, color, or type — just
> the essentials, using keyboard symbols you already know.

Alternative to restructured text format like it is used in
Sphinx-Documentations.

This service is documented using Markdown files inside the `docs/source`
folder.
The tools required for this documentation are [MkDocs](#mkdocs) and
[PyDoc-Markdown](#pydoc-markdown).

Documentation and useful additional resources:

* [Basic syntax](https://www.markdownguide.org/basic-syntax)
* [Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [GitHub: Mastering Markdown](https://guides.github.com/features/mastering-markdown/)


## MkDocs

From official documentation page:
> MkDocs is a fast, simple and downright gorgeous static site generator that's
> geared towards building project documentation.
> Documentation source files are written in Markdown, and configured with a
> single YAML configuration file.

It's mostly the same like Sphinx, but oriented on [Markdown](#markdown) and
a more modern output and usage design.

This service is documented using [PyDoc-Markdown](#pydoc-markdown) which is
a wrapper around MkDocs with additional functionality.

Documentation and useful additional resources:

* [MkDocs](https://www.mkdocs.org/)


## MkDocs-Material

Used theme in this service for [MkDocs](#mkdocs) (over
[PyDoc-Markdown](#pydoc-markdown)).

Documentation and useful additional resources:

* [Documentation](https://squidfunk.github.io/mkdocs-material/)


## OpenAPI

Description from wikipedia:
> The OpenAPI Specification, originally known as the Swagger Specification,
> is a specification for machine-readable interface files for describing,
> producing, consuming, and visualizing RESTful web services.
> Originally part of the Swagger framework, it became a separate project in
> 2016, overseen by the OpenAPI Initiative, an open-source collaboration
> project of the Linux Foundation.
> Swagger and some other tools can generate code, documentation and test cases
> given an interface file.

`OpenAPI`-documentations are sometimes yet named `Swagger`-documentations.

Used in the service to create the interactive documentation pages for the
service at routes:

* `/docs`
* `/redoc`

To create these documentation-pages, the package [FastAPI](#fastapi) is used.

Documentation and useful additional resources:

* [OpenAPI](https://www.openapis.org/)


## Poetry

Poetry is used in our workflow for python packaging and dependency management.
All relevant poetry commands like create new environment, update environment,
etc. are wrapped inside the `Makefile`, reducing the manual poetry commands to
execute to `poetry shell` when starting a new development-session.

Documentation and useful additional resources:

* [Poetry](https://poetry.eustace.io/docs/)


## Pre-Commit

Enables git-hooks for the service.
Is configured using the `.pre-commit-config.yml`.
Run a couple of linters, checkers and formatters like [Black](#black),
[Flake8](#flake8), [PyCodeStyle](#pycodestyle), etc.

Documentation and useful additional resources:

* [Documentation](https://pre-commit.com/)
* [Available hooks](https://pre-commit.com/hooks.html)


## Pydoc-Markdown

Pydocmd uses [MkDocs](#mkdocs) and extended [Markdown](#markdown) syntax to
generate Python API documentation.

Used in this service to create this documentation.
Configured inside the `pydocmd.yml`.
Markdown files used for the documentation are inside `docs/source`.

Documentation and useful additional resources:

* [Documentation](https://niklasrosenstein.github.io/pydoc-markdown/)


## PyDocStyle

Pydocstyle is a static analysis tool for checking compliance with Python
docstring conventions.

Used inside [pre-commit](#pre-commit) configured for the service in
`.pre-commit-config.yml`.

Documentation and useful additional resources:

* [Documentation](http://www.pydocstyle.org/en/latest/index.html)


## Pytest

Tests inside this service are using the pytest-package.

Tested code is easier to refactor and more stable.

Documentation and useful additional resources:

* [Pytest](https://pytest.org/en/latest/)
* [Pytest introduction](https://pythontesting.net/framework/pytest/pytest-introduction/)
* [Fixtures and Parameters](https://medium.com/ideas-at-igenius/fixtures-and-parameters-testing-code-with-pytest-d8603abb390a)
* [Python Testing](https://realpython.com/python-testing/)


## PyYAML

PyYAML is a full-featured [YAML](#yaml) framework for the Python programming
language.

Used inside [fastapi-serviceutils](#fastapi-serviceutils) to read the
`config.yml` to configure the service.
For additional information about how to configure the service see
[configuration](/configuration).

Documentation and useful additional resources:

* [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)


## Requests

Documentation and useful additional resources:

* [Requests](https://requests.kennethreitz.org/en/master/)


## Semantic Versioning (semver)

Services based on fastapi-serviceutils (like this service) use the
semantic-versioning style.
It is also named `SemVer`.
Alternative to other versioning styles like 0ver, CalVer, etc.

Semantic versioning in short:

A version is built of three elements separated by dots (even more elements are
possible but we are focusing on this short style in this service without
special cases like pre-releases, alpha, beta, etc.):
`<MAJOR>.<MINOR>.<PATCH>`

!!! note

    If a bugfix is made in the service, the `patch-version` will be increased.
    If additional functionality is added without changing previous behaviour of
    the service, the `minor-version` is increased.
    If breaking changes are made we increase the `major-version`.

The versioning style is defined in the `pyproject.toml` inside
`[tool.dephell.main]`.

Documentation and useful additional resources:

* [Semantic Versioning](https://semver.org/)


## SQLAlchemy

From official documentation:
> SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives
> application developers the full power and flexibility of SQL.
> 
> It provides a full suite of well known enterprise-level persistence
> patterns, designed for efficient and high-performing database access,
> adapted into a simple and Pythonic domain language.

This service uses [Databases](#databases) in combination with `SQLAlchemy` to
interact with databases.

Documentation and useful additional resources:

* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Most common commands](https://www.pythonsheets.com/notes/python-sqlalchemy.html)


## Tmux

tmux is a terminal multiplexer.
It lets you switch easily between several programs in one terminal, detach
them (they keep running in the background) and reattach them to a different
terminal.

It is used in the service during development in [Tmuxp](#tmuxp).

Documentation and useful additional resources:

* [Tmux](https://github.com/tmux/tmux/wiki)
* [Cheatsheet](https://tmuxcheatsheet.com/)
* [Tao of tmux](http://tmuxp.git-pull.com/en/latest/about_tmux.html)


## Tmuxp

Is a [tmux](#tmux) session manager.
Sessions and workflows can be configured inside a `.tmuxp.yml`.

This service contains such a `tmuxp.yml` for easier development.

Documentation and useful additional resources:

* [Tmuxp](https://tmuxp.git-pull.com/en/latest/)


## PyToolz

From official documentation:
> Toolz provides a set of utility functions for iterators, functions, and
> dictionaries.
> These functions interoperate well and form the building blocks of common
> data analytic operations.
> They extend the standard libraries itertools and functools and borrow
> heavily from the standard libraries of contemporary functional languages.
>
> Toolz provides a suite of functions which have the following functional
> virtues:
>
> * Composable: They interoperate due to their use of core data structures.
> * Pure: They don’t change their inputs or rely on external state.
> * Lazy: They don’t run until absolutely necessary, allowing them to support
>   large streaming data sets.
>
> Toolz functions are pragmatic.
> They understand that most programmers have deadlines.
>
> * Low Tech: They’re just functions, no syntax or magic tricks to learn
> * Tuned: They’re profiled and optimized
> * Serializable: They support common solutions for parallel computing
>
> This gives developers the power to write powerful programs to solve complex
> problems with relatively simple code.
> This code can be easy to understand without sacrificing performance.
> Toolz enables this approach, commonly associated with functional
> programming, within a natural Pythonic style suitable for most developers.

Toolz is used in [fastapi-serviceutils](#fastapi-serviceutils) on which this
service is based on.

It is recommended to use functions from this package in this service, too.

Documentation and useful additional resources:

* [PyToolz](https://toolz.readthedocs.io/en/latest/)


## Type Annotations

Also named type hints.
Annotate types of function- / method-parameters and return values to increase
readability and easier understanding of what a function requires and what it
produces.

Also used in [FastAPI](#fastapi) based services, like this service, to
generate the [OpenAPI](#openapi)-documentation.

Documentation and useful additional resources:

* [Type Annotations](https://docs.python.org/3/library/typing.html)
* [Using pythons type annotations](https://dev.to/dstarner/using-pythons-type-annotations-4cfe)
* [Cheatsheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)


## YAML

YAML is a human friendly data serialization standard for all programming
languages.

Mostly used for config-files.
Alternative to `JSON`-file format.

The `config.yml` of this service is such a yaml-file.
Inside the service (over [fastapi-serviceutils](#fastapi-serviceutils)) we use
[PyYAML](#pyyaml) to read the configuration-file (`config.yml`) of the service.

Documentation and useful additional resources:

* [yaml 1.2](https://yaml.org/spec/1.2/spec.html)
