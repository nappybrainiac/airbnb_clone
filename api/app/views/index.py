from app import app
from flask_json import json_response, jsonify
from app.models.base import *
from app.models.base import db
import datetime


@app.route('/', methods=['GET'])
def index():
    return json_response(
        status="OK",
        utc_time=datetime.datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S'),
        time=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    )


# Creating a connection to the database
@app.before_request
def before_request():
    db.connect()


# Database connections must always be closed
@app.after_request
def after_request(response):
    db.close()
    return response


# This function handles 404 errors.
@app.errorhandler(404)
def not_found(error):
    data = {
        'code': '404',
        'msg': 'not found'
    }
    error = jsonify(data)
    error.status_code = 404
    return error
    '''return json_response(code="404", msg="not found")'''
