from app import *
from config import *
from flask import Flask

'''
This is so that the code only executes
when it's running as the primary module
or intentionally called from another script.
'''
if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
