#!/usr/bin/python3
"""The City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City Class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City Class Initialization"""
        super().__init__(*args, **kwargs)
