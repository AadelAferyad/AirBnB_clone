#!usr/bin/python3
""" this file is for unittesting """


from models.review import Review
import unittest
import datetime


class ReviewTest(unittest.TestCase):
    """ test cases for Review class """

    def test_basic(self):
        """ basic test """
        rv = Review()
        self.assertEqual(type(rv), Review)
        self.assertIsInstance(rv.id, str)
        self.assertIsInstance(rv.created_at, datetime.datetime)
        self.assertIsInstance(rv.updated_at, datetime.datetime)

    def test_attributes(self):
        """ test attributes """
        rv = Review()
        rv.place_id = "dar houda"
        rv.user_id = "haruma"
        rv.text = "simple text"
        self.assertEqual(rv.place_id, "dar houda")
        self.assertEqual(rv.user_id, "haruma")
        self.assertEqual(rv.text, "simple text")


if __name__ == '__main__':
    unittest.main()
