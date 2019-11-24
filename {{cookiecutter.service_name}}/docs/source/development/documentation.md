# Documentation

The project's developer documentation is written using
[MKDocs](../../references/index.html#mkdocs) with
[Pydoc-Markdown](../../references/index.html#pydoc-markdown).

The documentation sources can be found in the `docs/source` subdirectory.

The API-documentation is auto-generated from the docstrings of modules,
classes, and functions.

These docstrings are written in
[markdown](../../references/index.html#markdown)-syntax.


## Modifying the documentation

To modify the documentation change the content of the markdown-file containing
the documentation section you want to change.

Then run the following command to create the new documentation:
```bash
    make docs
```

## Adding additional documentation pages

If additional documentation-pages are required, create a new markdown file
inside `docs/source` with the section name and add this section and file in
the `pydocmd.yml`.

Then run the following command to create the new documentation:
```bash
    make docs
```


## Adding new source-code (new python-file)

If you create an additional python-file (for example a new endpoint) write the
docstrings in this file using markdown-syntax.

Then add this file into the `generate`-section inside `pydocmd.yml`.
This triggers pydoc-markdown to extract the docstrings of this file and store
it into a new markdown file.
Also add this new file and the section-name at section
`pages`:`Source-Code Documentation`.
This triggers pydoc-markdown to include the page of this markdown file into
the documentation to create.

Then run the following command to create the new documentation:
```bash
    make docs
```


## Creating the documentation

To generate the documentation, run:
```bash
    make docs
```


## The documentation

After creating the documentation with `make docs` the generated HTML files can
be found at `docs/_build`.

!!! info

    If you want to serve the documentation locally after build to see what
    will be generated, run:
    ```
        PYTHONPATH=. pydocmd serve
    ```

There is also a [OpenAPI](../../references/index.html#openapi)-documentation
to be used for users of the service.
The documentation can be found at (after [running the
service](../running_service/index.html)):

* [http://0.0.0.0:{{cookiecutter.service_port}}/docs](http://0.0.0.0:{{cookiecutter.service_port}}/docs)
* [http://0.0.0.0:{{cookiecutter.service_port}}/redoc](http://0.0.0.0:{{cookiecutter.service_port}}/redoc)

The apidoc can be found at
[http://0.0.0.0:{{cookiecutter.service_port}}/apidoc/index.html](http://0.0.0.0:{{cookiecutter.service_port}}/apidoc/index.html).
