#!/usr/bin/python3
"""Module for file storage class."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State

class FileStorage:
    """
    File storage class.
    serializes instances into a JSON file
    and deserializes JSON file into instances
    """
    def __init__(self, file_path="file.json"):
        """initializes filestorage class."""
        self.file_path = file_path
        self.__objects = {}

    def all(self):
        """returns dictionary which contains all
        objects stored by FileStorage instance."""
        return self.__objects

    def new(self, obj):
        """sets an object in the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects into the json filepath."""
        save_dict = {}
        for key, obj in self.__objects.items():
            save_dict[key] = obj.to_dict()
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(save_dict, file)

    def reload(self):
        """deserializes the JSON file
        and loads objects into the __objects dictionary."""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
            "State": State
        }
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                dict_to_obj = json.load(file)
                for key, value in dict_to_obj.items():
                    class_name = value['__class__']
                    cls_to_instance = classes.get(class_name)
                    if cls_to_instance:
                        obj = cls_to_instance(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
