#!/usr/bin/python3
"""Tests for models/base_model.py.

    classes:
    TestBaseModel_to_dict
    TestBaseModel_save
    TestBaseModel_instantiation
    
"""
import datetime
import models
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_save(unittest.TestCase):
    """testing BaseModel class save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

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

    def test_one_save(self):
        _b_model = BaseModel()
        sleep(0.05)
        first_updated_at = _b_model.updated_at
        _b_model.save()
        self.assertLess(first_updated_at, _b_model.updated_at)

    def test_save_updates_file(self):
        _b_model = BaseModel()
        _b_model.save()
        bmid = "BaseModel." + _b_model.id
        with open("file.json", "r") as _file:
            self.assertIn(bmid, _file.read())

    def test_save_with_arg(self):
        _b_model = BaseModel()
        with self.assertRaises(TypeError):
            _b_model.save(None)

    def test_two_saves(self):
        _b_model = BaseModel()
        sleep(0.05)
        first_updated_at = _b_model.updated_at
        _b_model.save()
        second_updated_at = _b_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _b_model.save()
        self.assertLess(second_updated_at, _b_model.updated_at)


class TestBaseModel_instantiation(unittest.TestCase):
    """testing BaseModel class instantiation."""

    def test_args_unused(self):
        _b_model = BaseModel(None)
        self.assertNotIn(None, _b_model.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _b_model = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_b_model.id, "345")
        self.assertEqual(_b_model.created_at, _d_time)
        self.assertEqual(_b_model.updated_at, _d_time)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _b_model = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_b_model.id, "345")
        self.assertEqual(_b_model.created_at, _d_time)
        self.assertEqual(_b_model.updated_at, _d_time)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _b_model = BaseModel()
        _b_model.id = "123456"
        _b_model.created_at = _b_model.updated_at = _d_time
        bmstr = _b_model.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_two_models_different_created_at(self):
        base_mod1 = BaseModel()
        sleep(0.05)
        base_mod2 = BaseModel()
        self.assertLess(base_mod1.created_at, base_mod2.created_at)

    def test_two_models_different_updated_at(self):
        base_mod1 = BaseModel()
        sleep(0.05)
        base_mod2 = BaseModel()
        self.assertLess(base_mod1.updated_at, base_mod2.updated_at)

    def test_two_models_unique_ids(self):
        base_mod1 = BaseModel()
        base_mod2 = BaseModel()
        self.assertNotEqual(base_mod1.id, base_mod2.id)


class TestBaseModel_to_dict(unittest.TestCase):
    """testing BaseModel class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _b_model = BaseModel()
        self.assertNotEqual(_b_model.to_dict(), _b_model.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _b_model = BaseModel()
        _b_model.name = "Holberton"
        _b_model.my_number = 98
        self.assertIn("name", _b_model.to_dict())
        self.assertIn("my_number", _b_model.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _b_model = BaseModel()
        self.assertIn("id", _b_model.to_dict())
        self.assertIn("created_at", _b_model.to_dict())
        self.assertIn("updated_at", _b_model.to_dict())
        self.assertIn("__class__", _b_model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _b_model = BaseModel()
        bm_dict = _b_model.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _b_model = BaseModel()
        _b_model.id = "123456"
        _b_model.created_at = _b_model.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat()
        }
        self.assertDictEqual(_b_model.to_dict(), tdict)

    def test_to_dict_type(self):
        _b_model = BaseModel()
        self.assertTrue(dict, type(_b_model.to_dict()))

    def test_to_dict_with_arg(self):
        _b_model = BaseModel()
        with self.assertRaises(TypeError):
            _b_model.to_dict(None)


if __name__ == "__main__":
    unittest.main()

