'''
Project:    AirBnB Clone
File:       test/index.py
By:         Mackenzie Adams, Gloria Bwandungi

In this file we create our first test for the root of our Rest API.
'''

import unittest
import json
import time
from datetime import datetime
from app import app
from app.views import index

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        '''Creating a test client and ...'''
        self.app = app.test_client()
        '''propagating the exceptions to the test client'''
        self.app.testing = True

    def test_200(self):
          '''Is the HTTP response code equal == 200?'''
          rv = self.app.get('/')
          self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
