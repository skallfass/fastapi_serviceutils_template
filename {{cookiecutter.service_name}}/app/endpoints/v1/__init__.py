"""Collect the endpoints for version 1 inside the variable `ENDPOINTS`.

`ENDPOINTS` defined here is used inside `app.endpoints`.
"""

from fastapi_serviceutils.app.endpoints import set_version_endpoints

from app.endpoints.v1 import {{cookiecutter.endpoint}}


# combine the endpoints of version 1
ENDPOINTS = set_version_endpoints(
    endpoints=[{{cookiecutter.endpoint}}], version="v1", prefix_template="/api/{version}{route}"
)


__all__ = ["ENDPOINTS"]
