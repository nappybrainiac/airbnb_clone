'''
Project:    AirBnB Clone
File:       test/user.py
By:         Mackenzie Adams, Gloria Bwandungi

In this file we create our first test for the root of our Rest API.
'''

import unittest
import json
from app import app
import logging
from app.models.base import db
from app.models.user import User


class FlaskrTestCase_User(unittest.TestCase):

    def setUp(self):
        #creating a test client
        self.app = app.test_client()
        #disable logging
        logging.disable(logging.CRITICAL)
        #create User table
        db.create_tables([User], safe=True)

    def tearDown(self):
        #delete User table
        db.drop_tables([User], safe=True)

    def test_create(self):
        #send a POST request to app
        response = self.app.post('/users', data = dict(first_name = 'Jon',
                                                       last_name = 'Snow',
                                                       email = 'jon@snow.com',
                                                       password = 'first'))

        #send a POST request to app
        response = self.app.post('/users', data = dict(first_name = 'Jon',
                                                       last_name = 'Snow',
                                                       email = 'jon@snow.com',
                                                       password = 'first'))


    def test_list(self):
        pass

    def test_get(self):
        pass

    def test_delete(self):
        pass

    def test_update(self):
        pass
