#!/usr/bin/python3
"""Unit test for the Base class"""
import datetime
import pep8
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Test_BaseModel class"""

    def setUp(self):
        """ setup data for every test """
        self.test_base = BaseModel()

    def tearDown(self):
        """ clean the dat for the next test """
        pass

    def test_instance(self):
        """ test if an object is an instance from BaseModel """
        self.assertIsInstance(self.test_base, BaseModel)

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_doctring(self):
        """ Test doctrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)


    def test_str(self):
        """ Test str
        mockito = BaseModel()
        created = datetime.datetime(2019, 10, 10, 10, 10, 10, 10000)
        update = datetime.datetime(2019, 10, 10, 10, 10, 10, 10000)
        setattr(mockito, 'id', 'bf0b59b8-69a6-4b27-b9ff-49d48cce7f35')
        setattr(mockito, 'created_at', created)
        setattr(mockito, 'update_at', update) """
        
        self.assertIsNotNone(self.test_base)
