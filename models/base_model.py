#!/usr/bin/python3
"""Definition of the Base class for the application."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base class for the application project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseClass.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.identifier = str(uuid4())
        self.created_time = datetime.today()
        self.updated_time = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save_changes(self):
        """Update the updated_time with the current datetime."""
        self.updated_time = datetime.today()
        models.storage.save()

    def to_dictionary(self):
        """Return the dictionary representation of the BaseClass instance.

        with the key/value pair __class__ representing
        the object class name.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_time"] = self.created_time.isoformat()
        result_dict["updated_time"] = self.updated_time.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Return the print/str representation of the BaseClass instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.identifier, self.__dict__)

