#!/usr/bin/python3
"""
This module defines the FileStorage
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class for managing storage of instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object instance to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the stored objects to a JSON file
        """
        obj_dict = {}
        for obj in self.__objects:
            obj_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, mode="w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes objects from the JSON file back into the storage
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
