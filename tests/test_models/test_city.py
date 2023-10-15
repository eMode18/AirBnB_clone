#!/usr/bin/python3
"""Tests for models/city.py.

    classes:
    TestCity_save
    TestCity_to_dict
    TestCity_instantiation
"""
import os
from time import sleep
from models.city import City
import models
from datetime import datetime
import unittest


class TestCity_save(unittest.TestCase):
    """Testing City class save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

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
        _city = City()
        sleep(0.05)
        first_updated_at = _city.updated_at
        _city.save()
        self.assertLess(first_updated_at, _city.updated_at)

    def test_save_updates_file(self):
        _city = City()
        _city.save()
        cyid = "City." + _city.id
        with open("file.json", "r") as _file:
            self.assertIn(cyid, _file.read())

    def test_save_with_arg(self):
        _city = City()
        with self.assertRaises(TypeError):
            _city.save(None)

    def test_two_saves(self):
        _city = City()
        sleep(0.05)
        first_updated_at = _city.updated_at
        _city.save()
        second_updated_at = _city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _city.save()
        self.assertLess(second_updated_at, _city.updated_at)

class TestCity_instantiation(unittest.TestCase):
    """City class instantiation test."""

    def test_args_unused(self):
        _city = City(None)
        self.assertNotIn(None, _city.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_city.id, "345")
        self.assertEqual(_city.created_at, _d_time)
        self.assertEqual(_city.updated_at, _d_time)

    def test_name_is_public_class_attribute(self):
        _city = City()
        self.assertEqual(str, type(City.city_name))
        self.assertIn("name", dir(_city))
        self.assertNotIn("name", _city.__dict__)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_state_id_is_public_class_attribute(self):
        _city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(_city))
        self.assertNotIn("state_id", _city.__dict__)

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _city = City()
        _city.id = "123456"
        _city.created_at = _city.updated_at = _d_time
        cystr = _city.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_two_cities_different_created_at(self):
        _city1 = City()
        sleep(0.05)
        _city2 = City()
        self.assertLess(_city1.created_at, _city2.created_at)

    def test_two_cities_different_updated_at(self):
        _city1 = City()
        sleep(0.05)
        _city2 = City()
        self.assertLess(_city1.updated_at, _city2.updated_at)

    def test_two_cities_unique_ids(self):
        _city1 = City()
        _city2 = City()
        self.assertNotEqual(_city1.id, _city2.id)


class TestCity_to_dict(unittest.TestCase):
    """testing City class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _city = City()
        self.assertNotEqual(_city.to_dict(), _city.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _city = City()
        _city.middle_name = "Holberton"
        _city.my_number = 98
        self.assertEqual("Holberton", _city.middle_name)
        self.assertIn("my_number", _city.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _city = City()
        self.assertIn("id", _city.to_dict())
        self.assertIn("created_at", _city.to_dict())
        self.assertIn("updated_at", _city.to_dict())
        self.assertIn("__class__", _city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _city = City()
        cy_dict = _city.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _city = City()
        _city.id = "123456"
        _city.created_at = _city.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_city.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_with_arg(self):
        _city = City()
        with self.assertRaises(TypeError):
            _city.to_dict(None)


if __name__ == "__main__":
    unittest.main()

