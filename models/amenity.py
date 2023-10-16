#!/usr/bin/python3
"""Defines the Amenity Class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent the amenities.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
