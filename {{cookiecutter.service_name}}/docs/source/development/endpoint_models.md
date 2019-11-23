# Model-definition for an endpoint

Each endpoint has an input- and output-model definition.

These models inherit from `pydantic.BaseModel`.

Attributes of a model are defined using `Type Annotations`.

The models are defined inside `app/endpoints/<version of endpoint>/models.py`
and then imported and used inside the endpoints.


## Basic models

A basic input-model for an endpoint named `example` could be:

```python
    from pydantic import BaseModel


    class GetExample(BaseModel):
        name: str
```


A basic output-model for this endpoint could be:
```python
    from pydantic import BaseModel


    class Example(BaseModel):
        name: str
        age: int
        city: str
        street: str
        housenumber: str
```


## Complex models

More complex models could be defined like the following:
```python
from pydantic import BaseModel
from pydantic import Schema
from pydantic.dataclasses import dataclass


@dataclass
class Complex:
    """Represent example model with attribute-change of model after init."""
    mapped_attribute: str

    def __post_init_post_parse__(self) -> NoReturn:
        """Overwrite self.mapped_attribute with a mapping as defined below."""
        attribute_mapping = {
            'some': 'S',
            'other': 'O',
        }
        self.mapped_attribute = attribute_mapping[self.mapped_attribute]


def _alias_for_special_model_attribute(alias: str) -> str:
    """Use as ``alias_generator`` for models with special attribute-names."""
    return alias if not alias.endswith('_') else alias[:-1]


class SpecialParams(BaseModel):
    """Represent example model with special attribute name requiring alias."""
    msg: str
    schema_: str = Schema(None, alias='schema')

    class Config:
        """Required for special attribute ``schema``."""
        alias_generator = _alias_for_special_model_attribute
```
