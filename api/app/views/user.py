import flask
from app import app
from app.models.user import User
from app.models.base import db
import peewee
from flask import request, jsonify
import flask_json

'''To return a list of all users as a JSON object'''
@app.route('/users', methods=['GET', 'POST'])
def user_create_modify():
    if request.method == 'GET':
        user_list = User.select()
        #order_values = [i.to_hash for i in user_list]
        return jsonify(user_list)

    elif request.method == 'POST':
        ''' To get data from HTML form'''
        user_info = User.create(
            first_name = request.form['first_name'],
            last_name = request.form['last_name'],
            email = request.form['email'],
            password = ''
        )
        user_info.set_password(request.form['password'])
        return jsonify(user_info.to_hash())

"""def get_all_users():
    user_list = User.select()
    #order_values = [i.to_hash for i in user_list]
    return jsonify(user_list)"""

"""'''Create a new user. '''
@app.route('/users', methods=['POST'])
def create_new_user():
    ''' To get data from HTML form'''
    user_info = User.create(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        password = ''
    )
    user_info.set_password(request.form['password'])
    return jsonify(user_info.to_hash())"""
