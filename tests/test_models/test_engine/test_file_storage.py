#!/usr/bin/python3
"""
this file is for test case for file storage
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
import unittest
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """
    this class is for testing the file_storage
    class with some cases
    """

    def test_basic(self):
        """
        testing if the class is working basic test
        """
        instance_1 = FileStorage()
        self.assertEqual(type(instance_1), FileStorage)

    def test_attributes(self):
        """
        check if i can add attributes
        """
        instance_1 = FileStorage()
        instance_1.name = "Aadel"
        self.assertEqual(instance_1.__dict__["name"], "Aadel")
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_all_method(self):
        """
        test all method
        """
        dic = storage.all()
        self.assertEqual(type(dic), dict)

    def test_new_method(self):
        """
        test new method
        """
        base_instance = BaseModel()
        storage.new(base_instance)
        user_instance = User()
        storage.new(user_instance)
        place_instance = Place()
        storage.new(place_instance)
        city_instance = City()
        storage.new(city_instance)
        state_instance = State()
        storage.new(state_instance)
        review_instance = Review()
        storage.new(review_instance)
        amenity_instance = Amenity()
        storage.new(amenity_instance)
        dic = storage.all()
        self.assertIn("BaseModel." + base_instance.id, dic)
        self.assertIn("User." + user_instance.id, dic)
        self.assertIn("State." + state_instance.id, dic)
        self.assertIn("Place." + place_instance.id, dic)
        self.assertIn("City." + city_instance.id, dic)
        self.assertIn("Amenity." + amenity_instance.id, dic)
        self.assertIn("Review." + review_instance.id, dic)
        self.assertIn(base_instance, dic.values())
        self.assertIn(user_instance, dic.values())
        self.assertIn(state_instance, dic.values())
        self.assertIn(place_instance, dic.values())
        self.assertIn(city_instance, dic.values())
        self.assertIn(amenity_instance, dic.values())
        self.assertIn(review_instance, dic.values())

    def test_save_method(self):
        """
        test save method
        """
        base_instance = BaseModel()
        storage.new(base_instance)
        user_instance = User()
        storage.new(user_instance)
        place_instance = Place()
        storage.new(place_instance)
        city_instance = City()
        storage.new(city_instance)
        state_instance = State()
        storage.new(state_instance)
        review_instance = Review()
        storage.new(review_instance)
        amenity_instance = Amenity()
        storage.new(amenity_instance)
        dic = storage.all()
        storage.save()
        file_path = "file.json"
        if os.path.exists(file_path):
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        with open(file_path, "r", encoding="utf-8") as fd:
            data = fd.read()
            self.assertIn("BaseModel." + base_instance.id, data)
            self.assertIn("User." + user_instance.id, data)
            self.assertIn("State." + state_instance.id, data)
            self.assertIn("Place." + place_instance.id, data)
            self.assertIn("City." + city_instance.id, data)
            self.assertIn("Amenity." + amenity_instance.id, data)
            self.assertIn("Review." + review_instance.id, data)
        os.remove(file_path)
        storage.save()
        self.assertTrue(os.path.exists(file_path))

    def test_reload_method(self):
        """
        test for reload
        """
        base_instance = BaseModel()
        storage.new(base_instance)
        user_instance = User()
        storage.new(user_instance)
        place_instance = Place()
        storage.new(place_instance)
        city_instance = City()
        storage.new(city_instance)
        state_instance = State()
        storage.new(state_instance)
        review_instance = Review()
        storage.new(review_instance)
        amenity_instance = Amenity()
        storage.new(amenity_instance)
        storage.save()
        storage.reload()
        dic = storage.all()
        file_path = "file.json"
        self.assertIn("BaseModel." + base_instance.id, dic)
        self.assertIn("User." + user_instance.id, dic)
        self.assertIn("State." + state_instance.id, dic)
        self.assertIn("Place." + place_instance.id, dic)
        self.assertIn("City." + city_instance.id, dic)
        self.assertIn("Amenity." + amenity_instance.id, dic)
        self.assertIn("Review." + review_instance.id, dic)


if __name__ == "__main__":
    unittest.main()
