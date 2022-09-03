#!/usr/bin/python3
"""The Amenity Class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the Amenity Class"""
        super().__init__(*args, **kwargs)
