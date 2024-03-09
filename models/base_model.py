#!/usr/bin/python3
"""Module for baseModel class."""

from uuid import uuid4 
from datetime import datetime
import models

class BaseModel:
    """
    The baseModel class.
    """
    def __init__(self, *args, **kwargs):
        """Intitializes BaseModel class."""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == "updated_at":
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == "id":
                    self.id = str(value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """returns string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns dictionary representation of an instance"""
        dictionary = self.__dict__.copy() #make copy of dictionary representation
        dictionary ["__class__"] = type(self).__name__ #value of key is class name
        dictionary ["created_at"] = dictionary ["created_at"].isoformat() #key for created at
        dictionary ["updated_at"] = dictionary ["updated_at"].isoformat() #key for updated at

        return dictionary 
