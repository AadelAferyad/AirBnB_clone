#!usr/bin/python3
""" this file is for unittesting """


from models.review import Review
import unittest
import datetime
from models.base_model import BaseModel


class ReviewTest(unittest.TestCase):
    """ test cases for Review class """

    def test_basic(self):
        """ basic test """
        rv = Review()
        self.assertIsInstance(rv, Review)
        self.assertIsInstance(rv.id, str)
        self.assertIsInstance(rv.created_at, datetime.datetime)
        self.assertIsInstance(rv.updated_at, datetime.datetime)
        self.assertIsInstance(rv.place_id, str)
        self.assertIsInstance(rv.user_id, str)
        self.assertIsInstance(rv.text, str)

    def test_type(self):
        """test type"""
        rv = Review()
        self.assertEqual(rv.place_id, "")
        self.assertEqual(rv.user_id, "")
        self.assertEqual(rv.text, "")

    def test_attributes(self):
        """ test attributes """
        rv = Review()
        rv.place_id = "dar houda"
        rv.user_id = "haruma"
        rv.text = "simple text"
        self.assertEqual(rv.place_id, "dar houda")
        self.assertEqual(rv.user_id, "haruma")
        self.assertEqual(rv.text, "simple text")

    def test_inheritance(self):
        """test_inheritance"""
        self.assertTrue(issubclass(Review, BaseModel)
                        and Review is not BaseModel)


if __name__ == "__main__":
    unittest.main()
