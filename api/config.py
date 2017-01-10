
'''
    This configuration file sets up the variables
    for the AirBnB clone which has two different
    environments, development and production.


'''

import os


# For the production environment
if environ.get('AIRBNB_ENV') == 'production':
    DEBUG = False
    HOST = 0.0.0.0
    PORT = 3000
    DATABASE{
        'host': '158.69.80.153'
        'port': 3306
        'charset': utf8
        'user': 'airbnb_user_prod'
        'database': 'airbnb_prod'
        'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD')
    }

# For the development environment
if environ.get('AIRBNB_ENV') == 'development':
    DEBUG = True
    HOST = 'localhost'
    PORT = 3333
    DATABASE{
        'host': '158.69.80.153'
        'port': 3306
        'charset': utf8
        'user': 'airbnb_user_dev'
        'database': 'airbnb_dev'
        'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV')
    }
