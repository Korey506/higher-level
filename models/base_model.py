#!/usr/bin/python3
"""Airbnb project -- This is the base_model"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Defines all common attributes/methods for othe classes """

    def __init__(self, *args, **kwargs):
        """ initializes the public instances """

        if kwargs:
            for key, value in kwargs.items():

                """ check if the type(key) is a __class__, skip if yes """
                if key == "__class__":
                    continue

                """ convert the created_at and updated_at to objects """
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ string representation of the BaseModel class """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return (obj_dict)
