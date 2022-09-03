#!/usr/bin/python3
"""Test File for the file storage class"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json
from datetime import datetime


class TestFileStorageModel(unittest.TestCase):
    """Test Cases for the File storage model"""

    def setUp(self):
        self.f_storage = FileStorage()
        self.model = BaseModel()
        self.model_2 = BaseModel(id="12-345-678",
                                 created_at='2017-09-28T21:05:54.119427',
                                 updated_at='2017-09-28T21:05:54.119427')
        self.model_3 = BaseModel(id="1298-345-678908",
                                 created_at='2017-09-28T21:05:54.128445',
                                 updated_at='2017-09-28T21:05:54.128445')

        self.model_4 = BaseModel(id="1298-18765-678908",
                                 created_at='2017-09-28T21:05:54.120987',
                                 updated_at='2017-09-28T21:05:54.120987')
        return super().setUp()

    def tearDown(self):
        del(self.f_storage)
        del(self.model)
        del(self.model_2)
        del(self.model_3)
        del(self.model_4)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_filestorage_model(self):
        self.assertIsInstance(self.f_storage, FileStorage)

    def test_filestorage_model_attributes(self):

        with self.assertRaises(AttributeError):
            self.f_storage.__objects

        with self.assertRaises(AttributeError):
            self.f_storage.__file_path

    def test_filestorage_model_all(self):
        self.f_storage.new(self.model)
        class_name = type(self.model).__name__
        model_key = "{}.{}".format(class_name, self.model.id)
        data = self.f_storage.all()
        self.assertIsInstance(data, dict)
        self.assertIn(model_key, data.keys())

    def test_filestorage_model_new(self):
        class_name = type(self.model_2).__name__
        model_key = "{}.{}".format(class_name, self.model_2.id)
        data = self.f_storage.all()
        self.assertNotIn(model_key, data.keys())
        self.f_storage.new(self.model_2)
        self.assertIn(model_key, data.keys())

    def test_filestorage_model_save(self):
        class_name = type(self.model_3).__name__
        model_key = "{}.{}".format(class_name, self.model_3.id)
        self.f_storage.new(self.model_3)

        if os.path.exists("file.json"):
            with open("file.json", 'r', encoding="utf-8") as f:
                content = f.read()
                formattedContent = json.loads(content)
                self.assertNotIn(model_key, formattedContent.keys())

        self.f_storage.save()

        if os.path.exists("file.json"):
            with open("file.json", 'r', encoding="utf-8") as f:
                content = f.read()
                formattedContent = json.loads(content)
                self.assertIn(model_key, formattedContent.keys())

    def test_filestorage_model_reload(self):
        pass


if __name__ == '__main__':
    unittest.main()
