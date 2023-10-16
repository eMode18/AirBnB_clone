#!/usr/bin/python3
"""Review Class Definition."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent reviews.

    Attributes:
        place_id (str): The Place identifier.
        user_id (str): The User identifier.
        text (str): The review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
