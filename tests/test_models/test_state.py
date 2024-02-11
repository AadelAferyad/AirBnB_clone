#!usr/bin/python3
""" this file is for unittesting """


from models.state import State
import unittest
import datetime


class StateTest(unittest.TestCase):
    """ test cases for State class """

    def test_basic(self):
        """ basic test """
        state = State()
        self.assertEqual(type(state), State)

    def test_attributes(self):
        """ test attributes """
        st = State()
        self.assertEqual(st.name, "")
        self.assertIsInstance(st.id, str)
        self.assertIsInstance(st.created_at, datetime.datetime)
        self.assertIsInstance(st.updated_at, datetime.datetime)
        self.assertIsInstance(st.name, str)

    def test_with_value(self):
        """
        test assigning value to name
        """
        st = State()
        st.name = "Aadel"
        self.assertEqual(st.name, "Aadel")


if __name__ == '__main__':
    unittest.main()
