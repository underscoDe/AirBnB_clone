#!/usr/bin/python3
"""
    Module for user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represents a user

    Attributes;
    email: string - empty string for email
    password: string - empty string for password
    first_name: string - empty string for first name
    last_name: string - empty string for last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
