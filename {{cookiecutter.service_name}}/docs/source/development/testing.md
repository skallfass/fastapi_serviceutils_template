# Testing

For testing we use `pytest`, for details see
[Pytest Docs](http://doc.pytest.org/en/latest/).


All tests are located inside the folder `tests`.

Tests for a module should be names like `<MODULE_NAME>_test.py`.

To run all tests:

```bash
    make tests
```

A HTML coverage report is automatically created in the ``htmlcov`` directory.

!!! seealso

    For additional information how to test fastapi-applications:

    * [fastapi testing](https://fastapi.tiangolo.com/tutorial/testing/)
    * [fastapi testing-dependencies](https://fastapi.tiangolo.com/tutorial/testing-dependencies/)

    For information how to test async functions:

    * [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)
