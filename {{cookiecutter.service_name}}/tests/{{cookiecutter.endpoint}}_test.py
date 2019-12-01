from pathlib import Path

from fastapi_serviceutils import make_app
from fastapi_serviceutils.utils.tests.endpoints import json_endpoint

from app import __version__
from app.endpoints import ENDPOINTS


app = make_app(
    config_path=Path('app/config.yml'),
    version=__version__,
    endpoints=ENDPOINTS,
    enable_middlewares=[],
    additional_middlewares=[],
)


def test_endpoint_{{cookiecutter.endpoint}}():
    """Test if endpoints "/api/v1/{{cookiecutter.endpoint}}/" and "/api/latest/{{cookiecutter.endpoint}}/" work as expected."""
    for endpoint in [
            '/api/v1/{{cookiecutter.endpoint}}/',
            '/api/latest/{{cookiecutter.endpoint}}/'
    ]:
        json_endpoint(
            application=app,
            endpoint=endpoint,
            expected={'msg': 'test'},
            payload={'msg': 'test'}
        )
