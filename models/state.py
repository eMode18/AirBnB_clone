#!/usr/bin/python3
"""State Class Definition."""
from models.base_model import BaseModel


class State(BaseModel):
    """State representaion.

    Attributes:
        name (str): The state's name.
    """

    name = ""
