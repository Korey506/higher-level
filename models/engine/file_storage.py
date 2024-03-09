#!/usr/bin/python3
""" import json module """
import json
""" import os module """
from os import path
""" import all classes """
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ handles the storage of objects into a Json file """
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
                    class_type = globals().get(class_name)
                    if class_type:
                        self.__obj[key] = class_type(**value)
