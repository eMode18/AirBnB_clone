#!/usr/bin/python3
"""Tests for file_storage.py.
"""
import os
import json
from models.amenity import Amenity
from models.review import Review
import models
import unittest
from datetime import datetime
from models.place import Place
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State




class TestFileStorage_instantiation(unittest.TestCase):
    """testing of the FileStorage class instantiation."""

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorage_methods(unittest.TestCase):
    """testing of the FileStorage class methods."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        _model_base = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        _city = City()
        _amenity = Amenity()
        _review = Review()
        models.storage.new(_city)
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.new(_model_base)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        self.assertIn("User." + _user.id, models.storage.all().keys())
        self.assertIn(_user, models.storage.all().values())
        self.assertIn("State." + _state.id, models.storage.all().keys())
        self.assertIn(_state, models.storage.all().values())
        self.assertIn("BaseModel." + _model_base.id, models.storage.all().keys())
        self.assertIn(_model_base, models.storage.all().values())
        self.assertIn("Place." + _place.id, models.storage.all().keys())
        self.assertIn(_place, models.storage.all().values())
        self.assertIn(_amenity, models.storage.all().values())
        self.assertIn("Review." + _review.id, models.storage.all().keys())
        self.assertIn(_review, models.storage.all().values())
        self.assertIn("City." + _city.id, models.storage.all().keys())
        self.assertIn(_city, models.storage.all().values())
        self.assertIn("Amenity." + _amenity.id, models.storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        _city = City()
        _amenity = Amenity()
        _review = Review()
        _model_base = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        models.storage.new(_amenity)
        models.storage.new(_review)
        models.storage.save()
        models.storage.new(_model_base)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        save_text = ""
        with open("file.json", "r") as _file:
            save_text = _file.read()
            self.assertIn("BaseModel." + _model_base.id, save_text)
            self.assertIn("User." + _user.id, save_text)
            self.assertIn("State." + _state.id, save_text)
            self.assertIn("Place." + _place.id, save_text)
            self.assertIn("City." + _city.id, save_text)
            self.assertIn("Amenity." + _amenity.id, save_text)
            self.assertIn("Review." + _review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        _city = City()
        _amenity = Amenity()
        _review = Review()
        _model_base = BaseModel()
        _user = User()
        _state = State()
        _place = Place()
        models.storage.new(_review)
        models.storage.save()
        models.storage.reload()
        models.storage.new(_model_base)
        models.storage.new(_user)
        models.storage.new(_state)
        models.storage.new(_place)
        models.storage.new(_city)
        models.storage.new(_amenity)
        _objs = FileStorage._FileStorage__objects
        self.assertIn("City." + _city.id, _objs)
        self.assertIn("Amenity." + _amenity.id, _objs)
        self.assertIn("Review." + _review.id, _objs)
        self.assertIn("BaseModel." + _model_base.id, _objs)
        self.assertIn("User." + _user.id, _objs)
        self.assertIn("State." + _state.id, _objs)
        self.assertIn("Place." + _place.id, _objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
