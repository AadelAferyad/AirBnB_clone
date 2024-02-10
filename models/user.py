#!/usr/bin/python3
""" this file is for user class """


from .base_model import BaseModel


class User(BaseModel):
    """
    this class is for user data
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
