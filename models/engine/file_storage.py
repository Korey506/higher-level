#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel
"""
    The json  module let's us work with json files
    while the os module let's us work with the path function
"""


class FileStorage:
    __file_path = "file.json"
    __obj = {}

    def all(self):
        """ returns a dictionary obj """
        return self.__obj

    def new(self, obj):
        """ sets new object to the dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__obj[key] = obj

    def save(self):
        """ serialize __obj to a JSON file """
        serialized_objects = {}
        for key, value in self.__obj.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserialization """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__obj[key] = globals()[class_name](**value)
