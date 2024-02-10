#!/usr/bin/python3
""" this file is for file storage """


import os
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    this class is for serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        json_data = {}
        for key, value in FileStorage.__objects.items():
            json_data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            fd.write(json.dumps(json_data, indent=4))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                json_data = json.loads(fd.read())
                for key, value in json_data.items():
                    if '.' in key:
                        class_name, obj_id = key.split('.')
                        class_obj = globals()[class_name]
                        instance = class_obj(**value)
                        self.new(instance)
