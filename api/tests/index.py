from flask_json import JsonTestResponse
from app import app
import unittest
from datetime import datetime
from app.views import index
import json


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_200(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
