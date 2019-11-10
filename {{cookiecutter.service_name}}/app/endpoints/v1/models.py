"""Contain models required for the endpoint ``example`` (in version 1).

For models in fastapi-based services pydantic is used.
So each model inherits from :class:`BaseModel`.
"""

from pydantic import BaseModel


class GetExample(BaseModel):
    """Represent example model used for requests to example endpoint."""
    msg: str


class Example(BaseModel):
    """Represent example model used for response of example endpoint."""
    msg: str


__all__ = [
    'Example',
    'GetExample',
]
