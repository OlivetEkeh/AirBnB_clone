#!/usr/bin/python3
"""
Amenity module: Defines the amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class representing an amenity or feature.
    """
    name = ""
