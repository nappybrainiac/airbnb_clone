from flask_json import JsonTestResponse
from app import app
import unittest
from datetime import datetime
from app.views import index
import json


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.response_class = JsonTestResponse
        self.client = self.app.test_client()

    def test_200(self):
        res = self.client.get('/')
        assert res.status_code == 200, \
            "Status Code is NOT 200"

    def test_status(self):
        res = self.client.get('/')
        assert res.json['status'] == "OK", \
            "Status is NOT OK"

    def test_time(self):
        res = self.client.get('/')
        right_now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # changing time_dict from json to dictionary
        time_dict = json.loads(res.data)
        self.assertEqual(time_dict['time'], right_now)

    def test_time_utc(self):
        res = self.client.get('/')
        utc_time_now = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
        # changing utc_time_now from json to dictionary
        utc_dict = json.loads(res.data)
        self.assertEqual(utc_dict['utc_time'], utc_time_now)


if __name__ == '__main__':
    unittest.main()
