from fastapi_serviceutils.app.endpoints import set_version_endpoints

from app.endpoints.v1 import {{cookiecutter.endpoint}}


ENDPOINTS = set_version_endpoints(
    endpoints=[{{cookiecutter.endpoint}}],
    version='v1',
    prefix_template='/api/{version}{route}'
)


__all__ = ['ENDPOINTS']
