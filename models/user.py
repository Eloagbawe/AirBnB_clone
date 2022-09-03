#!/usr/bin/python3
"""The User Model Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialization for the user class"""
        super().__init__(*args, **kwargs)
