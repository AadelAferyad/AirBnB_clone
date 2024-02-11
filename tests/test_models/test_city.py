#!usr/bin/python3
""" this file is for unittesting """


from models.city import City
import unittest
from models.state import State
import datetime


class CityTest(unittest.TestCase):
    """ test cases for City class """

    def test_basic(self):
        """ basic test """
        cy = City()
        self.assertEqual(type(cy), City)

    def test_user_type(self):
        """
        test type
        """
        cy = City()
        self.assertEqual(cy.state_id, "")
        self.assertEqual(cy.name, "")
        self.assertIsInstance(cy.id, str)
        self.assertIsInstance(cy.created_at, datetime.datetime)
        self.assertIsInstance(cy.updated_at, datetime.datetime)
        self.assertIsInstance(cy.name, str)
        self.assertIsInstance(cy.state_id, str)

    def test_attributes(self):
        """ test attributes """
        cy = City()
        st = State()
        cy.state_id = st.id
        cy.name = "dar lkbira"

        self.assertEqual(cy.name, "dar lkbira")
        self.assertEqual(cy.state_id, st.id)


if __name__ == '__main__':
    unittest.main()
