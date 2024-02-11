#!/usr/bin/python3
"""
State module: defines the state class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representing a geographical state.
    """
    name = ""
