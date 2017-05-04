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
        test_res = self.client.get('/')
        assert test_res.status_code == 200, \
            "Status Code is NOT 200, or does not exist"

    def test_status(self):
        test_res = self.client.get('/')
        assert test_res.json['status'] == "OK", \
            "Status is NOT OK, or does not exist"


if __name__ == '__main__':
    unittest.main()
