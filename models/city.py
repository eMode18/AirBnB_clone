#!/usr/bin/python3
"""City Class Definition."""
from models.base_model import BaseModel


class City(BaseModel):
    """City representation.

    Attributes:
        state_identifier (str): The state identifier.
        city_name (str): The name of the city.
    """

    state_identifier = ""
    city_name = ""

