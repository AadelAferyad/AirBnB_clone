#!/usr/bin/python3
""" this file is for review class """


from .base_model import BaseModel


class Review(BaseModel):
    """ review class """

    place_id = ""
    user_id = ""
    text = ""
