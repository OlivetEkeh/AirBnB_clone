#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines the base model for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of a BaseModel."""
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, timeformat))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of dict of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def save(self):
        """
        Updates the public instance attribute updated_at with the current time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
