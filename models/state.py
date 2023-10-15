#!/usr/bin/python3
"""State Class Definition."""
from models.base_model import BaseModel


class State(BaseModel):
    """State representaion.

    Attributes:
        state_name (str): The name of the state.
    """

    state_name = ""
