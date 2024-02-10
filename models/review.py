#!/usr/bin/python3
"""This defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """this represent a review.

    Attributes:
        place_id (str): This is Place id.
        user_id (str): This is User id.
        text (str): This is text for the review.
    """

    place_id = ""
    user_id = ""
    text = ""
