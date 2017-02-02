'''
Project:    AirBnB Clone
File:       user.py
By:         Mackenzie Adams, Gloria Bwandungi

This file contains the app decorators that determine how users are viewed
added, and modified in the database.
'''

import flask
from app import app
from app.models.user import User
from app.models.base import db
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *


'''This function returns a list of users using the GET method and creates
   a new record using the POST method. '''
@app.route('/users', methods=['GET', 'POST'])
def user_create_modify():
    if request.method == 'GET':
        user_list = User.select()

        if user_list:
            order_values = [i.to_hash() for i in user_list]
            return jsonify(order_values)

        else:
            return jsonify(msg="There are no users in the database.")

    elif request.method == 'POST':
        ''' To get data from HTML form'''
        user_check = User.select().where(User.email == request.form['email'])

        if user_check:
            return jsonify(code=10000, msg="Email already exists."), 409

        else:
            user_info = User.create(
                first_name = request.form['first_name'],
                last_name = request.form['last_name'],
                email = request.form['email'],
                password = ''
            )
            user_info.set_password(request.form['password'])
            return jsonify(user_info.to_hash())

'''This function returns a user (by user_id), listing their attributes in JSON format using
   the GET method, modifies the record using PUT, and deletes it using DELETE '''
@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_user(user_id):
  user = User.select().where(User.id == user_id).first()

  if request.method == "GET":
      if user:
          return jsonify(user.to_hash())
      else:
          return jsonify(msg="User does not exist."), 404

  elif request.method == 'PUT':
      check_user = User.select().where(User.id == user_id).first()

      if not check_user:
          return jsonify(msg="User does not exist."), 404

      else:
          user_info = request.values
          for key in user_info:
              if key == 'updated_at' or key == 'created_at' or key == 'id':
                  continue
              if key == 'first_name':
                  user.first_name = user_info.get(key)
              if key == 'last_name':
                  user.last_name = user_info.get(key)
              if key == 'email' or key == 'is_admin':
                  return jsonify(msg="Email cannot be changed")
              if key == 'password':
                  user.password = user_info.get(key)

          user.save()
          return jsonify(user.to_hash())

  elif request.method == 'DELETE':
      user_info = User.get(User.id == user_id)
      user_info.delete_instance()
      user_info.save()
      return jsonify(msg="User deleted")
