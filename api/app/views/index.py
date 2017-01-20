from app import *
from flask_json import json_response
from app.models.base import *

import datetime



@app.route('/', methods=['GET'])

def index():
    return json_response(
    status="OK",
    utc_time=datetime.datetime.utcnow(),
    time=datetime.datetime.now()
    )

'''
Creating a connection to the database
'''
@app.before_request
def before_request():
    database.connect()

'''
Database connections must always be closed
'''
@app.after_request
def after_request(response):
    database.close()
    return response

'''
This function handles 404 errors.
'''
@app.errorhandler(404)
def not_found(e):
    return json_response(code="404", msg="not found")
