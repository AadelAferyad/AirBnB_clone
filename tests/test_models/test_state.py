#!usr/bin/python3
""" this file is for unittesting """


from models.state import State
import unittest
import datetime
from models.base_model import BaseModel


class StateTest(unittest.TestCase):
    """ test cases for State class """

    def test_basic(self):
        """ basic test """
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """ test attributes """
        st = State()
        self.assertIsInstance(st.id, str)
        self.assertIsInstance(st.created_at, datetime.datetime)
        self.assertIsInstance(st.updated_at, datetime.datetime)
        self.assertIsInstance(st.name, str)

    def test_type(self):
        """test type"""
        st = State()
        self.assertEqual(st.name, "")

    def test_with_value(self):
        """
        test assigning value to name
        """
        st = State()
        st.name = "Aadel"
        self.assertEqual(st.name, "Aadel")

    def test_inheritance(self):
        """test_inheritance"""
        self.assertTrue(issubclass(State, BaseModel)
                        and State is not BaseModel)


if __name__ == "__main__":
    unittest.main()
