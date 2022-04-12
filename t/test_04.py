#!/usr/bin/python3

import unittest
""" Classes
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User """
""" Methods """
from models.base_model import BaseModel
"""From models.engine.file_storage import FileStorage"""

class Test_04(unittest.TestCase):
    def test_01(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_02(self):
        bm1 = BaseModel()
        bm2 = BaseModel(**bm1.to_dict())
        self.assertEqual(bm1.id, bm2.id)
