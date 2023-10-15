#!/usr/bin/python3
"""User Class Definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """User representaion.

    Attributes:
        user_email (str): The email of the user.
        user_password (str): The password of the user.
        user_first_name (str): The first name of the user.
        user_last_name (str): The last name of the user.
    """

    user_email = ""
    user_password = ""
    user_first_name = ""
    user_last_name = ""
