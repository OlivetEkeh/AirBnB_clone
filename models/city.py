#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class inherited from base model

    The Public class attributes:
    state_id: string - empty string: this will be the State.id
    name: str - empty str
    """
    state_id = ""
    name = ""
    