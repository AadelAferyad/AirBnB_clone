#!/usr/bin/python3
"""
this file containe the base class
"""

from . import storage
from datetime import datetime
import uuid


class BaseModel:
    """
    the parent class that define all common
    attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of the class.

        Parameters:
        - *args: Not used.
        - **kwargs: Keyword arguments for initializing instance attributes.
            - If provided:
                - Set attributes using kwargs, excluding '__class__'.
                - Convert 'created_at' and 'updated_at' to datetime objects.
            - If not provided:
                - Generate a new UUID for 'id'.
                - Set 'created_at' and 'updated_at' to the current datetime.
                - Add the instance to the storage.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        for printing information about the class
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        method make a dictionary
        return :
            dictionary containing all keys/values of __dict__ of the instance
        """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)
