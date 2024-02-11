#!usr/bin/python3
""" this file is for unittesting """


from models.city import City
import unittest
from models.state import State


class CityTest(unittest.TestCase):
    """ test cases for City class """

    def test_basic(self):
        """ basic test """
        cy = City()
        self.assertEqual(type(cy), City)

    def test_user_type(self):
        cy = City()
        self.assertEqual(cy.state_id, "")
        self.assertEqual(cy.name, "")

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
