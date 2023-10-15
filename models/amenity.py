#!/usr/bin/python3
"""Defines the Amenity Class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent the amenities.

    Attributes:
        amenity_name (str): The name of the amenity.
    """

    amenity_name = ""
