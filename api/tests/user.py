from flask_json import JsonTestResponse
from app import app
import unittest
from app.models.base import db
from app.models.user import User
import json
import logging


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # create a test client
        self.app = app.test_client()
        # disable logging except for critical cases
        logging.disable(logging.CRITICAL)
        # create User table
        db.create_tables([User], safe=True)

    def tearDown(self):
        db.drop_table(User)

    def test_create(self):
        # post an account to User table
        self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='gigi',
            first_name='Gi',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 1)

        # post an account without an email address
        self.app.post('/users', data=dict(
            email='',
            password='zizi',
            first_name='zi',
            last_name='buju'
        ))
        self.assertEqual(User.select(id), 2)

        # post an account with same email address
        self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='sisi',
            first_name='sp',
            last_name='plix'
        ))
        self.assertEqual(User.select(id), 3)

        # post an account to User table
        self.app.post('/users', data=dict(
            email='zizi@jujubs.com',
            password='',
            first_name='Zee',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 4)

    def test_list(self):
        '''sends HTTP GET request to the app
           on a spsecified path'''
        res = self.app.get('/users')
        try:
            all_users = json.loads(res.data)
            # return the number of items in Users
            return len(all_users)
        except:
            return 0

    def test_get(self):
        # create a user and GET the user
        new_user = self.app.post('/users', data=dict(
                email='gigi@jujubs.com',
                password='yiyi',
                first_name='gigi',
                last_name='jujubs'
        ))
        # Checking the status code
        print new_user.status_code
        # Getting the user
        # checking if the user created is the same as the user returned
        # will return True is the  users match else will return false
        # checking when trying to get an id that is not linked to an user


if __name__ == '__main__':
    unittest.main()
