#!/usr/bin/python3
"""
Review module: defines the Review class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class representing a review for a place.
    """
    place_id = ""
    user_id = ""
    text = ""
