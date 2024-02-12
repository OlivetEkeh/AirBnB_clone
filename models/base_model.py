#!/usr/bin/python3
"""This is the BaseModel that defines all the common attributes $ methods for other classes"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """Attri: This is Date format used for date str conversion"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel
           Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        MY_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, MY_DATE_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a str representation of the BaseModel instance"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """Updates the attri and saves instance to storage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This Returns a dictionary representation of the BaseModel instance"""
        dicti = self.__dict__.copy()
        dicti['__class__'] = type(self).__name__
        dicti['created_at'] = self.created_at.isoformat()
        dicti['updated_at'] = self.updated_at.isoformat()
        return dicti
    