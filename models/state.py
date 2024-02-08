#!/usr/bin/python3
"""This defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This class represent a state.

    Attributes:
        name (str): this is the name of the state.
    """

    name = ""
