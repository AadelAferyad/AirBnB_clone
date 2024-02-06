#!/usr/bin/python3
""" this file is for file storage """
import os
import json


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            fd.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
                FileStorage.__objects = json.loads(fd.read())