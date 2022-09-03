#!/usr/bin/python3
"""The Base Model Class"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """The Base Model class"""

    def __init__(self, *args, **kwargs):
        """initialization"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, format))
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method"""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the updated at time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = type(self).__name__
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        # model_dict['created_at'] = self.created_at.isoformat()
        # model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
