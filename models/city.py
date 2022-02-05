#!/usr/bin/python3
"""Define city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city

    Attributes;
        state_id (str): id of the city
        name (str): name of the city
    """
    state_id = ""
    name = ""
