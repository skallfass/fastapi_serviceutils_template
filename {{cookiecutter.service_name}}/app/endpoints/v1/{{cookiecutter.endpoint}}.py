"""Endpoint definition for {{cookiecutter.endpoint}}."""
from fastapi import APIRouter
from fastapi import Body
from fastapi_serviceutils.app import Endpoint
from fastapi_serviceutils.app import create_id_logger
from starlette.requests import Request

from app.endpoints.v1.models import Example as Output
from app.endpoints.v1.models import GetExample as Input


ENDPOINT = Endpoint(router=APIRouter(), route='/{{cookiecutter.endpoint}}', version='v1')
SUMMARY = 'Example requests.'
EXAMPLE = Body(..., example={'msg': 'some message.'})


@ENDPOINT.router.post('/', response_model=Output, summary=SUMMARY)
async def {{cookiecutter.endpoint}}(
        request: Request,
        params: Input = EXAMPLE
) -> Output:
    _, log = create_id_logger(request=request, endpoint=ENDPOINT)
    log.debug(f'received request for {request.url} with params {params}.')
    return Output(msg=params.msg)
