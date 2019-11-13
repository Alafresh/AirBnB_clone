#!/usr/bin/python3
""" model user """
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class """

    """ public class attributes """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
