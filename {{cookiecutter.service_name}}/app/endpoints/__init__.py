"""Define routers to be available as endpoints in the service."""
from fastapi_serviceutils.endpoints import set_version_endpoints

from app.endpoints.v1 import ENDPOINTS as v1


LATEST = set_version_endpoints(
    endpoints=v1,
    version='latest',
    prefix_template='{route}'
)

ENDPOINTS = LATEST + v1

__all__ = ['ENDPOINTS']
