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
        bmodel = BaseModel()
        sleep(0.05)
        first_updated_at = bmodel.updated_at
        bmodel.save()
        self.assertLess(first_updated_at, bmodel.updated_at)

    def test_save_updates_file(self):
        bmodel = BaseModel()
        bmodel.save()
        bmid = "BaseModel." + bmodel.id
        with open("file.json", "r") as _file:
            self.assertIn(bmid, _file.read())

    def test_save_with_arg(self):
        bmodel = BaseModel()
        with self.assertRaises(TypeError):
            bmodel.save(None)

    def test_two_saves(self):
        bmodel = BaseModel()
        sleep(0.05)
        first_updated_at = bmodel.updated_at
        bmodel.save()
        second_updated_at = bmodel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bmodel.save()
        self.assertLess(second_updated_at, bmodel.updated_at)


class TestBaseModel_instantiation(unittest.TestCase):
    """testing BaseModel class instantiation."""

    def test_args_unused(self):
        bmodel = BaseModel(None)
        self.assertNotIn(None, bmodel.__dict__.values())

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
        bmodel = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmodel.id, "345")
        self.assertEqual(bmodel.created_at, _d_time)
        self.assertEqual(bmodel.updated_at, _d_time)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        bmodel = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bmodel.id, "345")
        self.assertEqual(bmodel.created_at, _d_time)
        self.assertEqual(bmodel.updated_at, _d_time)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        bmodel = BaseModel()
        bmodel.id = "123456"
        bmodel.created_at = bmodel.updated_at = _d_time
        bmstr = bmodel.__str__()
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
        bmodel = BaseModel()
        self.assertNotEqual(bmodel.to_dict(), bmodel.__dict__)

    def test_to_dict_contains_added_attributes(self):
        bmodel = BaseModel()
        bmodel.name = "Holberton"
        bmodel.my_number = 98
        self.assertIn("name", bmodel.to_dict())
        self.assertIn("my_number", bmodel.to_dict())

    def test_to_dict_contains_correct_keys(self):
        bmodel = BaseModel()
        self.assertIn("id", bmodel.to_dict())
        self.assertIn("created_at", bmodel.to_dict())
        self.assertIn("updated_at", bmodel.to_dict())
        self.assertIn("__class__", bmodel.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bmodel = BaseModel()
        bm_dict = bmodel.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        bmodel = BaseModel()
        bmodel.id = "123456"
        bmodel.created_at = bmodel.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat()
        }
        self.assertDictEqual(bmodel.to_dict(), tdict)

    def test_to_dict_type(self):
        bmodel = BaseModel()
        self.assertTrue(dict, type(bmodel.to_dict()))

    def test_to_dict_with_arg(self):
        bmodel = BaseModel()
        with self.assertRaises(TypeError):
            bmodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()

