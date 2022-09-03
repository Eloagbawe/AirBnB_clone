#!/usr/bin/python3
"""The State Model Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """The State Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State Class Initialization"""
        super().__init__(*args, **kwargs)
