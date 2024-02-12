#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Unittest for base model module.

This unittest is a collection of possible edge cases
on which this module should not be expected to fail,
and cases on which it is expected to fail.

"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        string = str(self.base_model)
        self.assertTrue(string.startswith("[BaseModel]"))
        self.assertIn("id: {}".format(self.base_model.id), string)
        self.assertIn("created_at: {}".format(self.base_model.created_at), string)
        self.assertIn("updated_at: {}".format(self.base_model.updated_at), string)

    def test_to_dict(self):
        self.base_model.name = "Test Model"
        self.base_model.my_number = 42
        self.base_model_dict = self.base_model.to_dict()
        self.assertEqual(self.base_model_dict['id'], self.base_model.id)
        self.assertEqual(self.base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(self.base_model_dict['name'], 'Test Model')
        self.assertEqual(self.base_model_dict['my_number'], 42)
        self.assertEqual(self.base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(self.base_model_dict['updated_at'], self.base_model.updated_at.isoformat())

    @patch('sys.stdout', new_callable=StringIO)
    def test_save(self, mock_stdout):
        self.base_model.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            data = json.load(file)
            key = "BaseModel." + self.base_model.id
            self.assertIn(key, data)
            self.assertEqual(data[key]['id'], self.base_model.id)
            self.assertEqual(data[key]['__class__'], 'BaseModel')
            self.assertEqual(data[key]['created_at'], self.base_model.created_at.isoformat())
            self.assertEqual(data[key]['updated_at'], self.base_model.updated_at.isoformat())
        expected_output = "Warning: models.storage is not accessible.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
