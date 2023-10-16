#!/usr/bin/python3
"""User Class Definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """User representaion.

    Attributes:
        email (str): users email address.
        password (str): Users password.
        first_name (str): The users first name.
        last_name (str): The users last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
