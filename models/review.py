#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherited from BaseModel.

    Public class attri:
    place_id: str - empty str: this will be the Place.id
    user_id: str - empty str: this will be the User.id
    text: str - empty str
    """

    place_id = ""
    user_id = ""
    text = ""
    