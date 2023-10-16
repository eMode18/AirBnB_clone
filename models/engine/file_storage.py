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

    def new(self, obj):
        """Add obj to the objects dictionary with key <obj_class_name>.id."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize the objects dictionary to the JSON file at __file_path."""
        object_dict = FileStorage.__objects
        s_dict = {obj: object_dict[obj].to_dict() for obj
                  in object_dict.keys()}
        with open(FileStorage.__file_path, "w") as _file:
            json.dump(s_dict, _file)

    def reload(self):
        """Deserialize the JSON file at __file_path
        into the objects dictionary, if it exists."""
        try:
            with open(FileStorage.__file_path) as _file:
                object_dict = json.load(_file)
                for item in object_dict.values():
                    class_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            return
