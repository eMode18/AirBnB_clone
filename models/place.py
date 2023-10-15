#!/usr/bin/python3
"""Place Class Definition."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a location.

    Attributes:
        city_identifier (str): The City identifier.
        user_identifier (str): The User identifier.
        place_name (str): The name of the place.
        place_description (str): The description of the place.
        room_count (int): The number of rooms of the place.
        bathroom_count (int): The number of bathrooms of the place.
        max_guest_count (int): The maximum number of guests of the place.
        night_price (int): The price by night of the place.
        latitude_value (float): The latitude of the place.
        longitude_value (float): The longitude of the place.
        amenity_identifiers (list): A list of Amenity identifiers.
    """

    city_identifier = ""
    user_identifier = ""
    place_name = ""
    place_description = ""
    room_count = 0
    bathroom_count = 0
    max_guest_count = 0
    night_price = 0
    latitude_value = 0.0
    longitude_value = 0.0
    amenity_identifiers = []

