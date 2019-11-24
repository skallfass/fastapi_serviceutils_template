# Versioning of endpoints

To support backwards compatibility the endpoints are versioned.

This means if changes in an endpoint result in different behaviour of the
endpoint, or the input- and output-models change (in semantic-versioning we
create a major-update), we define these changes inside a new version-folder.

For example if we currently have an endpoint `example` and we want to change
its output-model, we would create a new `feature-branch`
(see [git-workflow](../git_workflow/index.html)) and inside this feature-branch we create
a new folder `v2`.
The resulting folder-structure would look like:

```bash
├── app
│   ├── config.yml
│   ├── endpoints
│   │   ├── __init__.py
│   │   ├── v1
│   │   │   ├── errors.py
│   │   │   ├── example.py
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   └── v2
│   │       ├── errors.py
│   │       ├── example.py
│   │       ├── __init__.py
│   │       └── models.py
│   ├── __init__.py
│   └── main.py
```

Then we could develop like default inside the `v2`-folder and finally
committing the content of `v2`, the `v1` folder is kept untouched.
