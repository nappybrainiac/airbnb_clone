from flask import Flask
from flask_json import FlaskJSON

# to initialize app
app = Flask(__name__)
json = FlaskJSON(app)

from views import *
