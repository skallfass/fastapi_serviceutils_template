# References

Collection of references, blogs, documentation pages for used packages, tools.


## Black

Code formatter for python.
Used during development of this service inside [pre-commit](#pre-commit).

As described in official documentation:
> Blackened code looks the same regardless of the project you're reading.
> Formatting becomes transparent after a while and you can focus on the
> content instead.
>
> Black makes code review faster by producing the smallest diffs possible.

Documentation and useful additional resources:

* [black](https://black.readthedocs.io/en/stable/)


## codespell

Check misspellings in code.
Used during development of this service inside [pre-commit](#pre-commit).

Documentation and useful additional resources:

* [codespell](https://github.com/codespell-project/codespell)


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

Documentation and useful additional resources:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pep8](https://www.python.org/dev/peps/pep-0008/)
* [pep8 the style guide for python code](https://pep8.org/)


## git

Git is a free and open source distributed version control system.

For additional information about the git-workflow used in this service see
[git-workflow](../development/git_workflow)

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
Jlog-entries, the default logging of fastapi is extended by usage of loguru
inside services based on fastapi-serviceutils.

Documentation and useful additional resources:

* [Loguru](https://loguru.readthedocs.io/en/stable/index.html)


## Make

To wrap common tasks during development of the service, commands are wrapped
inside a makefile.
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

Documentation and useful additional resources:

* [MkDocs](https://www.mkdocs.org/)


## MkDocs-Material

Used theme in this service for [MkDocs](#mkdocs).

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

Documentation and useful additional resources:


## PyDoc-Markdown

Documentation and useful additional resources:


## PyDocStyle

Documentation and useful additional resources:


## Pytest
Tests inside this service are using the pytest-package.

Tested code is easier to refactor and more stable.
This topic focuses on pytest as the most used and easiest to use
testing-package for python.

* https://pythontesting.net/framework/pytest/pytest-introduction/
* https://medium.com/ideas-at-igenius/fixtures-and-parameters-testing-code-with-pytest-d8603abb390a
* https://realpython.com/python-testing/
* https://docs.pytest.org/en/latest/

Documentation and useful additional resources:

* [Pytest](https://pytest.org/en/latest/)


## PyYAML

Documentation and useful additional resources:

* [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)



## Requests

Documentation and useful additional resources:

* [Requests](https://requests.kennethreitz.org/en/master/)


## Semantic Versioning (semver)

Services based on fastapi-serviceutils (like this service) use the
semantic-versioning style.

Documentation and useful additional resources:

* [semver](https://semver.org/)


## SQLAlchemy

Documentation and useful additional resources:

* [SQLAlchemy](https://www.sqlalchemy.org/)


## Tmux

Documentation and useful additional resources:

* [Tmux](https://github.com/tmux/tmux/wiki)


## Tmuxp

Documentation and useful additional resources:

* [Tmuxp](https://tmuxp.git-pull.com/en/latest/)


## PyToolz

Documentation and useful additional resources:

* [PyToolz](https://toolz.readthedocs.io/en/latest/)


## Type Annotations

Documentation and useful additional resources:

* [Type Annotations](https://docs.python.org/3/library/typing.html)


## YAML

Inside the service we use [PyYAML](#pyyaml) to read the configuration-file
(`config.yml`) for the service.

Documentation and useful additional resources:

* [yaml 1.2](https://yaml.org/spec/1.2/spec.html)
