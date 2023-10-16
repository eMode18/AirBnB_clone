#!/usr/bin/python3
"""Tests for models/place.py.

    classes:
    TestPlace_to_dict
    TestPlace_instantiation
    TestPlace_save
"""
import os
from time import sleep
from models.place import Place
import models
from datetime import datetime
import unittest


class TestPlace_save(unittest.TestCase):
    """testing Place class save method."""

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
        _place = Place()
        sleep(0.05)
        first_updated_at = _place.updated_at
        _place.save()
        self.assertLess(first_updated_at, _place.updated_at)

    def test_save_updates_file(self):
        _place = Place()
        _place.save()
        plid = "Place." + _place.id
        with open("file.json", "r") as _file:
            self.assertIn(plid, _file.read())

    def test_save_with_arg(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.save(None)

    def test_two_saves(self):
        _place = Place()
        sleep(0.05)
        first_updated_at = _place.updated_at
        _place.save()
        second_updated_at = _place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _place.save()
        self.assertLess(second_updated_at, _place.updated_at)

class TestPlace_instantiation(unittest.TestCase):
    """testing Place class instantiation."""

    def test_args_unused(self):
        _place = Place(None)
        self.assertNotIn(None, _place.__dict__.values())

    def test_city_id_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(_place))
        self.assertNotIn("city_id", _place.__dict__)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_description_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(_place))
        self.assertNotIn("description", _place.__dict__)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _place = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_place.id, "345")
        self.assertEqual(_place.created_at, _d_time)
        self.assertEqual(_place.updated_at, _d_time)

    def test_max_guest_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(_place))
        self.assertNotIn("max_guest", _place.__dict__)

    def test_name_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(_place))
        self.assertNotIn("name", _place.__dict__)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_number_bathrooms_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(_place))
        self.assertNotIn("number_bathrooms", _place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(_place))
        self.assertNotIn("number_rooms", _place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(_place))
        self.assertNotIn("price_by_night", _place.__dict__)

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _place = Place()
        _place.id = "123456"
        _place.created_at = _place.updated_at = _d_time
        plstr = _place.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_two_places_different_created_at(self):
        _place1 = Place()
        sleep(0.05)
        _place2 = Place()
        self.assertLess(_place1.created_at, _place2.created_at)

    def test_two_places_different_updated_at(self):
        _place1 = Place()
        sleep(0.05)
        _place2 = Place()
        self.assertLess(_place1.updated_at, _place2.updated_at)

    def test_two_places_unique_ids(self):
        _place1 = Place()
        _place2 = Place()
        self.assertNotEqual(_place1.id, _place2.id)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_user_id_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(_place))
        self.assertNotIn("user_id", _place.__dict__)



class TestPlace_to_dict(unittest.TestCase):
    """testing Place class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _place = Place()
        self.assertNotEqual(_place.to_dict(), _place.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _place = Place()
        _place.middle_name = "Holberton"
        _place.my_number = 98
        self.assertEqual("Holberton", _place.middle_name)
        self.assertIn("my_number", _place.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _place = Place()
        self.assertIn("id", _place.to_dict())
        self.assertIn("created_at", _place.to_dict())
        self.assertIn("updated_at", _place.to_dict())
        self.assertIn("__class__", _place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _place = Place()
        pl_dict = _place.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _place = Place()
        _place.id = "123456"
        _place.created_at = _place.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_place.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_with_arg(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.to_dict(None)


if __name__ == "__main__":
    unittest.main()

