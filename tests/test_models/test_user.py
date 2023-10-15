#!/usr/bin/python3
"""Tests for models/user.py.

    classes:
    TestUser_instantiation
    TestUser_to_dict
    TestUser_save
"""
import os
from time import sleep
from models.user import User
import models
from datetime import datetime
import unittest


class TestUser_save(unittest.TestCase):
    """testing of the  class save method."""

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
        _user = User()
        sleep(0.05)
        first_updated_at = _user.updated_at
        _user.save()
        self.assertLess(first_updated_at, _user.updated_at)

    def test_save_updates_file(self):
        _user = User()
        _user.save()
        usid = "User." + _user.id
        with open("file.json", "r") as _file:
            self.assertIn(usid, _file.read())

    def test_save_with_arg(self):
        _user = User()
        with self.assertRaises(TypeError):
            _user.save(None)

    def test_two_saves(self):
        _user = User()
        sleep(0.05)
        first_updated_at = _user.updated_at
        _user.save()
        second_updated_at = _user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _user.save()
        self.assertLess(second_updated_at, _user.updated_at)

class TestUser_instantiation(unittest.TestCase):
    """testing of the User class instantiation."""

    def test_args_unused(self):
        _user = User(None)
        self.assertNotIn(None, _user.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_user.id, "345")
        self.assertEqual(_user.created_at, _d_time)
        self.assertEqual(_user.updated_at, _d_time)

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _user = User()
        _user.id = "123456"
        _user.created_at = _user.updated_at = _d_time
        usstr = _user.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_two_users_different_created_at(self):
        _user1 = User()
        sleep(0.05)
        _user2 = User()
        self.assertLess(_user1.created_at, _user2.created_at)

    def test_two_users_different_updated_at(self):
        _user1 = User()
        sleep(0.05)
        _user2 = User()
        self.assertLess(_user1.updated_at, _user2.updated_at)

    def test_two_users_unique_ids(self):
        _user1 = User()
        _user2 = User()
        self.assertNotEqual(_user1.id, _user2.id)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))



class TestUser_to_dict(unittest.TestCase):
    """testing of the User class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _user = User()
        self.assertNotEqual(_user.to_dict(), _user.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _user = User()
        _user.middle_name = "Holberton"
        _user.my_number = 98
        self.assertEqual("Holberton", _user.middle_name)
        self.assertIn("my_number", _user.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _user = User()
        self.assertIn("id", _user.to_dict())
        self.assertIn("created_at", _user.to_dict())
        self.assertIn("updated_at", _user.to_dict())
        self.assertIn("__class__", _user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _user = User()
        us_dict = _user.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _user = User()
        _user.id = "123456"
        _user.created_at = _user.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_user.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_with_arg(self):
        _user = User()
        with self.assertRaises(TypeError):
            _user.to_dict(None)


if __name__ == "__main__":
    unittest.main()

