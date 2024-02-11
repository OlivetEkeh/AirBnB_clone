#!/usr/bin/python3
"""
City module: defines the city class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class representing a city in a geographical state.
    """
    state_id = ""
    name = ""
