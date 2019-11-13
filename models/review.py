#!/usr/bin/python3
""" model review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class """

    """ public class attributes """
    place_id = ''
    user_id = ''
    text = ''
