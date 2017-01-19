from datetime import datetime
from flask_json import json_response
import peewee
from app import app
import datetime
from app.models.base import BaseModel, database


@app.route('/', methods=['GET'])
'''
The browser tells the server to just get
the information stored on that page and
send it. This is probably the most common
method.
'''
def index():
    return json_response(
    status="OK",
    utc_time=datetime.utcnow(),
    time=datetime.now()
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
def after_request():
    database.close()

'''
This function handles 404 errors.
'''
@app.errorhandler(404)
def not_found(e):
    return json_response(code="404", msg="not found")
