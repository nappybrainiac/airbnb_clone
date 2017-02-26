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
          resp = self.app.get('/')
          self.assertEqual(resp.status_code, 200)

    def test_status(self):
        '''Is the JSON reponse status == OK?'''
        resp = self.app.get('/')
        resp_data = json.loads(resp.data)
        self.assertEqual(resp_data.get("status"), "OK")

    def test_time(self):
        '''Is the JSON reponse time == time right now?'''
        resp = self.app.get('/')
        now = datetime.now().strftime("%Y/%m/%d %H:%M")
        try:
            right_now = datetime.strptime(resp.json['time'], "%Y/%m/%d %H:%M:%S")
        except ValueError as err:
            print "The HTTP response 'time' format is incorrect."
        self.assertEqual(now, right_now.strftime("%Y/%m/%d %H:%M"))

    def test_time_utc(self):
        '''Is the JSON reponse time == time right now?'''
        resp = self.app.get('/')
        now = datetime.now().strftime("%Y/%m/%d %H:%M")
        try:
            right_now = datetime.strptime(resp.json['time'], "%Y/%m/%d %H:%M:%S")
        except ValueError as err:
          print "The HTTP response 'time' format is incorrect."
        self.assertEqual(now, right_now.strftime("%Y/%m/%d %H:%M"))




if __name__ == '__main__':
    unittest.main()
