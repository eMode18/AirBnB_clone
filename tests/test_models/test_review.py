#!/usr/bin/python3
"""Tests for models/review.py.

    classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
from time import sleep
from models.review import Review
import models
from datetime import datetime
import unittest


class TestReview_save(unittest.TestCase):
    """testing Review class save method."""

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
        _review = Review()
        sleep(0.05)
        first_updated_at = _review.updated_at
        _review.save()
        self.assertLess(first_updated_at, _review.updated_at)

    def test_save_updates_file(self):
        _review = Review()
        _review.save()
        rvid = "Review." + _review.id
        with open("file.json", "r") as _file:
            self.assertIn(rvid, _file.read())

    def test_save_with_arg(self):
        _review = Review()
        with self.assertRaises(TypeError):
            _review.save(None)

    def test_two_saves(self):
        _review = Review()
        sleep(0.05)
        first_updated_at = _review.updated_at
        _review.save()
        second_updated_at = _review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _review.save()
        self.assertLess(second_updated_at, _review.updated_at)

class TestReview_instantiation(unittest.TestCase):
    """testing Review class instantiation."""

    def test_args_unused(self):
        _review = Review(None)
        self.assertNotIn(None, _review.__dict__.values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        _d_time = datetime.today()
        dt_iso = _d_time.isoformat()
        _review = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(_review.id, "345")
        self.assertEqual(_review.created_at, _d_time)
        self.assertEqual(_review.updated_at, _d_time)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id_is_public_class_attribute(self):
        _review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(_review))
        self.assertNotIn("place_id", _review.__dict__)

    def test_str_representation(self):
        _d_time = datetime.today()
        dt_repr = repr(_d_time)
        _review = Review()
        _review.id = "123456"
        _review.created_at = _review.updated_at = _d_time
        rvstr = _review.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_text_is_public_class_attribute(self):
        _review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(_review))
        self.assertNotIn("text", _review.__dict__)

    def test_two_reviews_different_created_at(self):
        _review1 = Review()
        sleep(0.05)
        _review2 = Review()
        self.assertLess(_review1.created_at, _review2.created_at)

    def test_two_reviews_different_updated_at(self):
        _review1 = Review()
        sleep(0.05)
        _review2 = Review()
        self.assertLess(_review1.updated_at, _review2.updated_at)

    def test_two_reviews_unique_ids(self):
        _review1 = Review()
        _review2 = Review()
        self.assertNotEqual(_review1.id, _review2.id)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_user_id_is_public_class_attribute(self):
        _review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(_review))
        self.assertNotIn("user_id", _review.__dict__)



class TestReview_to_dict(unittest.TestCase):
    """testing Review class to_dict method."""

    def test_contrast_to_dict_dunder_dict(self):
        _review = Review()
        self.assertNotEqual(_review.to_dict(), _review.__dict__)

    def test_to_dict_contains_added_attributes(self):
        _review = Review()
        _review.middle_name = "Holberton"
        _review.my_number = 98
        self.assertEqual("Holberton", _review.middle_name)
        self.assertIn("my_number", _review.to_dict())

    def test_to_dict_contains_correct_keys(self):
        _review = Review()
        self.assertIn("id", _review.to_dict())
        self.assertIn("created_at", _review.to_dict())
        self.assertIn("updated_at", _review.to_dict())
        self.assertIn("__class__", _review.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _review = Review()
        rv_dict = _review.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        _d_time = datetime.today()
        _review = Review()
        _review.id = "123456"
        _review.created_at = _review.updated_at = _d_time
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': _d_time.isoformat(),
            'updated_at': _d_time.isoformat(),
        }
        self.assertDictEqual(_review.to_dict(), tdict)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_with_arg(self):
        _review = Review()
        with self.assertRaises(TypeError):
            _review.to_dict(None)


if __name__ == "__main__":
    unittest.main()

