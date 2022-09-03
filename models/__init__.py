#!/usr/bin/python3
"""initialization file for models"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel,
           "User": User,
           "City": City,
           "Place": Place,
           "State": State,
           "Amenity": Amenity,
           "Review": Review
           }

storage = FileStorage()
storage.reload()
