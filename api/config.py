
'''
Project:    AirBnB Clone
File:       config.py
By:         Mackenzie Adams, Gloria Bwandungi


This configuration file sets up the variables
for the AirBnB clone which has three different
environments, testing, development & production.
'''

import os


# For the production environment
if os.environ.get('AIRBNB_ENV') == 'production':
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 3000
    DATABASE = {
        'host': '158.69.80.153',
        'port': 3306,
        'charset': 'utf8',
        'user': 'airbnb_user_prod',
        'database': 'airbnb_prod',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD')
    }

# For the development environment
if os.environ.get('AIRBNB_ENV') == 'development':
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE = {
        'host': '158.69.80.153',
        'port': 3306,
        'charset': 'utf8',
        'user': 'airbnb_user_dev',
        'database': 'airbnb_dev',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')
    }

# For the testing environments
if os.environ.get('AIRBNB_ENV') == 'test':
    DEBUG = True
    HOST = 'localhost'
    PORT = 5555
    DATABASE = {
        'host': '158.69.80.153',
        'port': 3306,
        'charset': 'utf8',
        'user': 'airbnb_user_test',
        'database': 'airbnb_test',
        'password': os.environ.get('AIRBNB_DATABASE_PWD_TEST')
    }
