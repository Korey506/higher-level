#!/usr/bin/python3
""" import json module """
import json
from os import path
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
    __objects = {}

    def all(self):
        """ returns a dictionary obj """
        return FileStorage.__objects

    def new(self, obj):
        """ sets new object to the dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serialize __obj to a JSON file """
        serialized_objects = {}
        for key, value in FileStorage.__objects.item():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file_:
            json.dump(serialized_objects, file_)

    def reload(self):
        """ Deserialization """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file_:
                data = json.load(file_)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_type = globals().get(class_name)
                    if class_type:
                        FileStorage.__objects[key] = class_type(**value)
