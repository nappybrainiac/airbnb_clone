from flask_json import JsonTestResponse
from app import app
import unittest
from app.models.base import db
from app.models.user import User
import json
import logging


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        # create a test client
        self.app = app.test_client()
        self.app.response_class = JsonTestResponse
        # disable logging except for critical cases
        logging.disable(logging.CRITICAL)
        # create User table
        db.create_tables([User], safe=True)

    def test_user_status_code(self):
        # testing to check the status code of a simple GET
        # request from 'localhost:3333/users'
        user_res = self.app.get('/users')
        self.assertEqual(user_res.status_code, 200,
                         '/users is not returning anything.')

    def test_create(self):
        # post an account to User table
        self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='gigi',
            first_name='Gi',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 1, 'user account not created')

        # post an account without an email address
        self.app.post('/users', data=dict(
            email='',
            password='zizi',
            first_name='zi',
            last_name='buju'
        ))
        self.assertEqual(User.select(id), 2,  'user account not created')

        # post an account with same email address
        self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='sisi',
            first_name='sp',
            last_name='plix'
        ))
        self.assertEqual(User.select(id), 3,  'user account not created')

        # post an account to User table
        self.app.post('/users', data=dict(
            email='zizi@jujubs.com',
            password='',
            first_name='Zee',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 4,  'user account not created')

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
        assertEqual(res.status_code, 200)

    def test_get(self):
        new_acct = self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='gigi',
            first_name='Gi',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 1, 'user account not created')
        res = self.app.get('/users/1').data
        # verify that the new_acct is the same as res
        self.assertEqual(sorted(res), sorted(new_acct.data),
                         'new account is not the same as what\'s listed')

        # try accessing an account that doesn't exist.
        # res = self.app.get('/users/3')
        # assert res.status_code == 404

    def test_update(self):
        new_acct = self.app.post('/users', data=dict(
            email='gigi@jujubs.com',
            password='gigi',
            first_name='Gi',
            last_name='Jubs'
        ))
        self.assertEqual(User.select(id), 1, 'user account not created')
        res = self.app.get('/users/1').data
        # verify that the new_acct is the same as res
        self.assertEqual(sorted(res), sorted(new_acct.data),
                         'new account is not the same as what\'s listed')
        # update it.
        trial = self.app.put('/users/1', data=dict(email='geegee@jujubz.edu'))
        # check status code
        updated_acct = self.app.get('/users/1')
        assert b'geegee@jujubz.edu' not in trial.data

        # try updating an account that doesn't exist.
        bad_update = self.app.put('/users/2', data=dict(first_name='Laturu'))
        self.assertEqual(bad_update.status_code, 404, 'user does not exist')

    def tearDown(self):
        db.drop_table(User)


if __name__ == '__main__':
    unittest.main()
