#!/usr/bin/python3

import uuid
from datetime import datetime

"""
    uuid - for generating universal unique ID
    datetime - to genrate current date and time an instance is created
"""
class BaseModel():
    """ Defines all common attributes/methods for othe classes """

    def __init__(self):
        """ initializes the public instances """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ string representation of the BaseModel class """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return (obj_dict)
