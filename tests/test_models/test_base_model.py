#!/usr/bin/python3
""" this file is for test casess of BaseModel class"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    this class is for testing
    the BaseModel class using various test cases
    """

    def test_attribute(self):
        """
        test the basic attributes are initilazed
        """
        instance_1 = BaseModel()
        v = getattr(instance_1, "id", 0)
        self.assertTrue(instance_1.id == v)
        v = getattr(instance_1, "created_at", 0)
        self.assertTrue(instance_1.created_at == v)
        v = getattr(instance_1, "updated_at", 0)
        self.assertTrue(instance_1.updated_at == v)

    def test_type(self):
        """
        test basic attributes types
        """
        instance_1 = BaseModel()
        a = datetime.now()
        self.assertTrue(type(instance_1.id) == str)
        self.assertTrue(type(instance_1.created_at) == type(a))
        self.assertTrue(type(instance_1.updated_at) == type(a))

    def test_unique_id(self):
        """
        test two ids are the equals
        """
        instance_1 = BaseModel()
        inctance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, inctance_2.id)

    def test_str(self):
        """
        test magic method
        """
        instance_1 = BaseModel()
        strr = ("[{}] ({}) {}".format(instance_1.__class__.__name__,
                instance_1.id, instance_1.__dict__))
        self.assertEqual(str(instance_1), strr)

    def test_save_method(self):
        """
        test save method
        """
        instance_1 = BaseModel()
        update = instance_1.updated_at
        instance_1.save()
        self.assertNotEqual(update, instance_1.updated_at)

    def test_to_dict(self):
        """
        test to_dict() method
        """
        instance_1 = BaseModel()
        instance_1.name = "Aadel"
        dic = instance_1.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(dic["name"], "Aadel")
        self.assertEqual(type(dic["created_at"]), str)

    def test_kwargs(self):
        """
        test passing kwargs to BaseModel()
        """
        instance_1 = BaseModel()
        instance_1.name = "houda"
        dic = instance_1.to_dict()
        instance_2 = BaseModel(**dic)
        self.assertNotEqual(instance_1, instance_2)
        self.assertEqual(instance_1.id, instance_2.id)


if __name__ == "__main__":
    unittest.main()
