"""Define routers to be available as endpoints in the service.

This includes the endpoints for each version and also the latest-endpoints.
"""
from fastapi_serviceutils.app.endpoints import set_version_endpoints

from app.endpoints.v1 import ENDPOINTS as v1


# set the latest endpoints to "api/latest/<endpoint>"
LATEST = set_version_endpoints(
    endpoints=v1, version="latest", prefix_template="{route}"
)

# combine all endpoints to be used in `make_app` inside `main.py`
ENDPOINTS = LATEST + v1

__all__ = ["ENDPOINTS"]
