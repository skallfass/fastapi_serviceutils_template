# Overview

[![Generic badge](https://img.shields.io/badge/Python-3.7-green.svg)](https://shields.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Generic badge](https://img.shields.io/badge/Using-poetry-blue.svg)](https://github.com/sdispater/poetry)
[![Generic badge](https://img.shields.io/badge/Using-PreCommit-grey.svg)](https://pre-commit.com/)
![coverage](apidoc/coverage.svg)


## Service subject-specific documentation

To learn more about the functionality and logic of the service see
[Subject-specific documentation](apidoc/subject_specific_documentation/index.html).


## Development

This service uses a strict and predefined development workflow (like
code-style, focused on clean code, a fixed git-workflow, dependency isolation
in virtual environments using poetry, etc.) as defined in
the `development`-section.

The `Development`-documentation contains the following sections:

* [Getting started](apidoc/development/getting_started/index.html)
* [Dependency management](apidoc/development/dependency_management/index.html)
* [Git-workflow](apidoc/development/git_workflow/index.html)
* [Configuration](apidoc/configuration/index.html)
* [Documentation](apidoc/development/documentation/index.html)
* [Testing](apidoc/development/testing/index.html)
* Endpoints
    * [Endpoint structure](apidoc/development/endpoint_structure/index.html)
    * [Endpoint model-definition](apidoc/development/endpoint_models/index.html)
    * [Endpoint versioning](apidoc/development/versioning/index.html)
* Helpers
    * [Makefile](apidoc/development/helpers/makefile/index.html)
    * [Pre-Commit](apidoc/development/helpers/pre-commit/index.html)
    * [Tmuxp](apidoc/development/helpers/tmuxp/index.html)
* [Running service](apidoc/development/running_service/index.html)
* [Recommended additional resources](apidoc/recommended/index.html)

To achieve this it is based on a couple of packages and tools
(see [references](apidoc/references/index.html) for a complete list and details).


## Deployment

`Deployment` of this service is done inside `docker-containers`
(see [deployment](apidoc/deployment/index.html) for details).
