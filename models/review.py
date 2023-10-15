#!/usr/bin/python3
"""Review Class Definition."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent reviews.

    Attributes:
        place_identifier (str): The Place identifier.
        user_identifier (str): The User identifier.
        review_text (str): The text of the review.
    """

    place_identifier = ""
    user_identifier = ""
    review_text = ""
