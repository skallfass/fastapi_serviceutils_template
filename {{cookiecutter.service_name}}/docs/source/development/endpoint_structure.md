# Structure of an endpoint file

Each endpoint is defined in its own file inside `app/endpoints/<version of
endpoint>/<endpoint-name>.py` (for details about versioning see
[versioning](versioning)).

Each endpoint has his own input- and output-model definition inside
`app/endpoints/<version of endpoint>/models.py` (for details see
[models](endpoint_models)).

A basic endpoint looks like:
```python
"""Endpoint definition for example."""
from fastapi import APIRouter
from fastapi import Body
from fastapi_serviceutils.app import Endpoint
from fastapi_serviceutils.app import create_id_logger
from starlette.requests import Request

from app.endpoints.v1.models import Example
from app.endpoints.v1.models import GetExample


ENDPOINT = Endpoint(router=APIRouter(), route='/example', version='v1')
SUMMARY = 'Example requests.'
EXAMPLE = Body(..., example={'name': 'John Doe'})


@ENDPOINT.router.post('/', response_model=Output, summary=SUMMARY)
async def example(request: Request, params: GetExample = EXAMPLE) -> Example:
    """Example docstring for an endpoint.

    # Parameters:
        request (Request): the original request.
        params (GetExample): the request-params converted to an instance of
            `GetExample`.

    # Returns:
        (Example) the processed result for this endpoint as an instance of
        `Example`.

    """
    _, log = create_id_logger(request=request, endpoint=ENDPOINT)
    log.debug(f'received request for {request.url} with params {params}.')

    age, city, street, housenumber = await some_extraction_function(name=params.name)
    return Example(
        name=params.name,
        age=age,
        city=city,
        street=street,
        housenumber=housenumber
    )
```


## ENDPOINT

The variable `ENDPOINT` defines the endpoint and is required and used for
function `set_version_endpoints` from `fastapi-serviceutils` (inside
`app/endpoints/<version of endpoint>/__init__.py` and
`app/endpoints/__init__.py`).


### ENDPOINT.route

The `route`-attribute of `ENDPOINT` defines the route-suffix for this endpoint.
It is modified inside `app/endpoints/<version of endpoint>/__init__.py`:
```python
from fastapi_serviceutils.app.endpoints import set_version_endpoints

from app.endpoints.v1 import example


ENDPOINTS = set_version_endpoints(
    endpoints=[example],
    version='v1',
    prefix_template='/api/{version}{route}'
)
```

This means this endpoint is available on route `/api/v1/example`.

Inside `app/endpoints/__init__.py` an additional route for this endpoint under
`latest` is added:
```python
"""Define routers to be available as endpoints in the service."""
from fastapi_serviceutils.app.endpoints import set_version_endpoints

from app.endpoints.v1 import ENDPOINTS as v1


LATEST = set_version_endpoints(
    endpoints=v1,
    version='latest',
    prefix_template='{route}'
)

ENDPOINTS = LATEST + v1
```


### ENDPOINT.version

The attribute `version` of `ENDPOINT` is the same like the version-folder of
this endpoint.


## SUMMARY

The `SUMMARY` is required for the OpenAPI-documentation of the endpoint.
It should describe in short what this endpoint does.


## EXAMPLE

The `EXAMPLE` is an instance of `fastapi.Body` and is used as example value
for the OpenAPI-documentation of the endpoint.


## The endpoint-function

### decorator

The decorator `ENDPOINT.router.post` register the endpoint for the APIRouter.
In this example it is used like:
```python
@ENDPOINT.router.post('/', response_model=Output, summary=SUMMARY)
```
Here we define the response_model to be used for the output of this endpoint
and that we want to show the summary as defined in `SUMMARY` for the
OpenAPI-documentation of this endpoint.

### parameters of the endpoint-function
```python
async def example(request: Request, params: GetExample = EXAMPLE) -> Example:
```
requires the parameters `request` as an instance of
`starlette.requests.Request`.
This request-variable is used to create the request-id for the current request
to be used in the logger to be able to differentiate between different requests
inside the log-file.
It is used in:
```python
    _, log = create_id_logger(request=request, endpoint=ENDPOINT)
    log.debug(f'received request for {request.url} with params {params}.')
```
Logging with this `log` uses the request-id of this request in log-entries.

The next parameter `params` contains the request-parameters passed to the
endpoint converted to an instance of the defined input-model (in this case
`GetExample`).
Because this is a class, you can access its attributes using `.`.
For example we can access the request-parameter `name` in this example using
`params.name`.

The type annotation of the return value of this function shows (like in the
decorator `response_model`) that this function returns an instance of the
output-model (in this case `Example`).

!!! note

    In fact the function does not have to return an instance of the
    output-model, it can also be a dict containing the same content as an
    instance of the output-model.


### docstring

The docstring is defined using markdown to be able to extract it using
pydoc-markdown when running `make docs`.


### processing logic

The part
```python
    age, city, street, housenumber = await some_extraction_function(name=params.name)
```
is only an example.
Here you would place the processing logic of the endpoint.
Try to use async-functions here and call them with `await` to let your
endpoint be as asynchronous as possible.


### combining the output
Finally (after the processing logic) we combine the output of the endpoint to
be returned to the client.
In this example this would be:
```python
    return Example(
        name=params.name,
        age=age,
        city=city,
        street=street,
        housenumber=housenumber
    )
```
