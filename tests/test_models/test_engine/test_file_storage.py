#!/usr/bin/python3
"""Tests for models/engine/file_storage.py.

    classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import models
import unittest
from models.state import State
from models.place import Place



class TestFileStorage_instantiation(unittest.TestCase):
    """testing of the FileStorage class instantiation."""

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))




class TestFileStorage_methods(unittest.TestCase):
    """testing of the FileStorage class methods."""

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)


    def test_new(self):
        _b_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_b_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        self.assertIn("BaseModel." + _b_model.id, models.storage.all().keys())
        self.assertIn(_b_model, models.storage.all().values())
        self.assertIn("User." + _user.id, models.storage.all().keys())
        self.assertIn(_user, models.storage.all().values())
        self.assertIn("State." + _state.id, models.storage.all().keys())
        self.assertIn(_state, models.storage.all().values())
        self.assertIn("Place." + _place.id, models.storage.all().keys())
        self.assertIn(_place, models.storage.all().values())
        self.assertIn("City." + _city.id, models.storage.all().keys())
        self.assertIn(_city, models.storage.all().values())
        self.assertIn("Amenity." + _amenity.id, models.storage.all().keys())
        self.assertIn(_amenity, models.storage.all().values())
        self.assertIn("Review." + _review.id, models.storage.all().keys())
        self.assertIn(_review, models.storage.all().values())

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        _b_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_b_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.save()
        models.storage.reload()
        _objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + _b_model.id, _objs)
        self.assertIn("User." + _user.id, _objs)
        self.assertIn("State." + _state.id, _objs)
        self.assertIn("Place." + _place.id, _objs)
        self.assertIn("City." + _city.id, _objs)
        self.assertIn("Amenity." + _amenity.id, _objs)
        self.assertIn("Review." + _review.id, _objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save(self):
        _b_model = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_b_model)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as _file:
            save_text = _file.read()
            self.assertIn("BaseModel." + _b_model.id, save_text)
            self.assertIn("User." + _user.id, save_text)
            self.assertIn("State." + _state.id, save_text)
            self.assertIn("Place." + _place.id, save_text)
            self.assertIn("City." + _city.id, save_text)
            self.assertIn("Amenity." + _amenity.id, save_text)
            self.assertIn("Review." + _review.id, save_text)


if __name__ == "__main__":
    unittest.main()
