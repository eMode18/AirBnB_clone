import datetime
import os
import unittest
from models.amenity import Amenity
import models
from time import sleep

class TestAmenity_instantiation(unittest.TestCase):
    """testing Amenity class instantiation."""
    
    def test_args_unused(self):
        _amenity = Amenity(None)
        self.assertNotIn(None, _amenity.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        """instantiating with kwargs test method"""
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_amenity.id, "345")
        self.assertEqual(_amenity.created_at, _d_time)
        self.assertEqual(_amenity.updated_at, _d_time)

    def test_name_is_public_class_attribute(self):
        _amenity = Amenity()
        self.assertEqual(str, type(Amenity.amenity_name))
        self.assertIn("amenity_name", dir(Amenity()))
        self.assertNotIn("amenity_name", _amenity.__dict__)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _amenity = Amenity()
        _amenity.id = "123456"
        _amenity.created_at = _amenity.updated_at = _d_time
        amstr = _amenity.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_two_amenities_different_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

class TestAmenity_save(unittest.TestCase):
    """testing Amenity class save method."""

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
        _amenity = Amenity()
        sleep(0.05)
        first_updated_at = _amenity.updated_at
        _amenity.save()
        self.assertLess(first_updated_at, _amenity.updated_at)

    def test_save_updates_file(self):
        _amenity = Amenity()
        _amenity.save()
        amid = "Amenity." + _amenity.id
        with open("file.json", "r") as _file:
            self.assertIn(amid, _file.read())

    def test_save_with_arg(self):
        _amenity = Amenity()
        with self.assertRaises(TypeError):
            _amenity.save(None)

    def test_two_saves(self):
        _amenity = Amenity()
        sleep(0.05)
        first_updated_at = _amenity.updated_at
        _amenity.save()
        second_updated_at = _amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _amenity.save()
        self.assertLess(second_updated_at, _amenity.updated_at)

class TestAmenity_to_dict(unittest.TestCase):
    """testing Amenity class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _amenity = Amenity()
        self.assertNotEqual(_amenity.to_dict(), _amenity.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _amenity = Amenity()
        _amenity.middle_name = "Holberton"
        _amenity.my_number = 98
        self.assertEqual("Holberton", _amenity.middle_name)
        self.assertIn("my_number", _amenity.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _amenity = Amenity()
        self.assertIn("id", _amenity.to_dict())
        self.assertIn("created_at", _amenity.to_dict())
        self.assertIn("updated_at", _amenity.to_dict())
        self.assertIn("__class__", _amenity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _amenity = Amenity()
        am_dict = _amenity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _amenity = Amenity()
        _amenity.id = "123456"
        _amenity.created_at = _amenity.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_amenity.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_with_arg(self):
        _amenity = Amenity()
        with self.assertRaises(TypeError):
            _amenity.to_dict(None)

if __name__ == "__main__":
    unittest.main()

