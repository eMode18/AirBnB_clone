#!/usr/bin/python3
"""Test for models/state.py.

    classes:
    TestState_to_dict
    TestState_instantiation
    TestState_save
"""
import os
from time import sleep
from models.state import State
import models
from datetime import datetime
import unittest


class TestState_to_dict(unittest.TestCase):
    """testing of the State class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _state = State()
        self.assertNotEqual(_state.to_dict(), _state.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _state = State()
        _state.middle_name = "Holberton"
        _state.my_number = 98
        self.assertEqual("Holberton", _state.middle_name)
        self.assertIn("my_number", _state.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _state = State()
        self.assertIn("id", _state.to_dict())
        self.assertIn("created_at", _state.to_dict())
        self.assertIn("updated_at", _state.to_dict())
        self.assertIn("__class__", _state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _state = State()
        st_dict = _state.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _state = State()
        _state.id = "123456"
        _state.created_at = _state.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_state.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_with_arg(self):
        _state = State()
        with self.assertRaises(TypeError):
            _state.to_dict(None)

class TestState_instantiation(unittest.TestCase):
    """testing of the State class instantiation."""

    def test_args_unused(self):
        _state = State(None)
        self.assertNotIn(None, _state.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_state.id, "345")
        self.assertEqual(_state.created_at, _d_time)
        self.assertEqual(_state.updated_at, _d_time)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_name_is_public_class_attribute(self):
        _state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(_state))
        self.assertNotIn("name", _state.__dict__)

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _state = State()
        _state.id = "123456"
        _state.created_at = _state.updated_at = _d_time
        ststr = _state.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_two_states_different_created_at(self):
        _state1 = State()
        sleep(0.05)
        _state2 = State()
        self.assertLess(_state1.created_at, _state2.created_at)

    def test_two_states_different_updated_at(self):
        _state1 = State()
        sleep(0.05)
        _state2 = State()
        self.assertLess(_state1.updated_at, _state2.updated_at)

    def test_two_states_unique_ids(self):
        _state1 = State()
        _state2 = State()
        self.assertNotEqual(_state1.id, _state2.id)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))


class TestState_save(unittest.TestCase):
    """testing of the State class save method."""

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
        _state = State()
        sleep(0.05)
        first_updated_at = _state.updated_at
        _state.save()
        self.assertLess(first_updated_at, _state.updated_at)

    def test_save_updates_file(self):
        _state = State()
        _state.save()
        stid = "State." + _state.id
        with open("file.json", "r") as _file:
            self.assertIn(stid, _file.read())

    def test_save_with_arg(self):
        _state = State()
        with self.assertRaises(TypeError):
            _state.save(None)

    def test_two_saves(self):
        _state = State()
        sleep(0.05)
        first_updated_at = _state.updated_at
        _state.save()
        second_updated_at = _state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _state.save()
        self.assertLess(second_updated_at, _state.updated_at)


if __name__ == "__main__":
    unittest.main()

