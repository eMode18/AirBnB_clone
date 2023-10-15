#!/usr/bin/python3
"""Defines the Storage class for file handling."""
import json
from models.city import City
from models.place import Place
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents a file storage engine.

    Attributes:
        __file_path (str): The file path for storing objects.
        __objects (dict): A dictionary containing instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve the dictionary of objects."""
        return FileStorage.__objects

    def new(self, _obj):
        """Add _obj to the objects dictionary with key <obj_class_name>.id."""
        class_name = _obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, _obj.id)] = _obj

    def save(self):
        """Serialize the objects dictionary to the JSON file at __file_path."""
        object_dict = FileStorage.__objects
        serialized_dict = {_obj: object_dict[_obj].to_dict() for _obj in object_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserialize the JSON file at __file_path 
        into the objects dictionary, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                object_dict = json.load(file)
                for _obj in object_dict.values():
                    class_name = _obj["__class__"]
                    del _obj["__class__"]
                    self.add(eval(class_name)(**_obj))
        except FileNotFoundError:
            return

