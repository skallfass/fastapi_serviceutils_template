# Getting started

After cloning the repository the development environment can be initialized
using:

```bash
    cd <PROJECT-DIRECTORY>
    poetry shell
    make init
```

This will create the pyenv environment for this project.

Activate it.

!!! note

    Make sure to always activate the environment when you start
    working on the project in a new terminal using

    ```
        poetry shell
    ```


To update dependencies and `poetry.lock` use:

```bash
    make update
```

This also creates `requirements.txt` to be used for Docker_.
