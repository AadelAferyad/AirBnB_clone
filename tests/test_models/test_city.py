#!usr/bin/python3
""" this file is for unittesting """


from models.city import City
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class CityTest(unittest.TestCase):
    """ test cases for City class """

    def test_basic(self):
        """ basic test """
        cy = City()
        self.assertIsInstance(cy, City)

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

    def test_inheritance(self):
        """test_inheritance"""
        self.assertTrue(issubclass(City, BaseModel)
                        and City is not BaseModel)


if __name__ == "__main__":
    unittest.main()
