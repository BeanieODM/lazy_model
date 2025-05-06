from pydantic import Field, field_validator, model_validator

from lazy_model import LazyModel


class Simple(LazyModel):
    i: int
    s: str

    @field_validator("s")
    def s_upper(cls, v):
        return v.upper()

    @model_validator(mode="before")
    def check_card_number_omitted(cls, values):
        return values


class Nested(LazyModel):
    s: Simple
    lst: list[Simple]


class Inherited(Simple):
    f: float


class WithAlias(LazyModel):
    i: int = Field(alias="_i_alias")
