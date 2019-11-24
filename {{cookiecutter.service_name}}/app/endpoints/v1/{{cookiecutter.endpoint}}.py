"""Endpoint definition for {{cookiecutter.endpoint}}."""
from fastapi import APIRouter
from fastapi import Body
from fastapi_serviceutils.app import create_id_logger
from fastapi_serviceutils.app import Endpoint
from starlette.requests import Request

from app.endpoints.v1.models import Example
from app.endpoints.v1.models import GetExample


ENDPOINT = Endpoint(router=APIRouter(), route="/{{cookiecutter.endpoint}}", version="v1")
SUMMARY = "Example requests."
EXAMPLE = Body(..., example={"msg": "some message."})


@ENDPOINT.router.post("/", response_model=Example, summary=SUMMARY)
async def {{cookiecutter.endpoint}}(request: Request, params: GetExample = EXAMPLE) -> Example:
    """Example docstring.

    #Parameters:
        request (Request): the original request.
        params (Example): the request-parameters converted to an instance of
            `Example`.

    # Returns:
        (GetExample) the result for the request.

    """
    _, log = create_id_logger(request=request, endpoint=ENDPOINT)
    log.debug(f"received request for {request.url} with params {params}.")
    return Example(msg=params.msg)
