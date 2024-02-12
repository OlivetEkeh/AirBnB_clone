#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class inherits from BaseModel.

    The Public class attributes:
    email: str - empty str
    password: str - empty str
    first_name: str - empty str
    last_name: str - empty str
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    