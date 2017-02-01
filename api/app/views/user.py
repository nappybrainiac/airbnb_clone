import flask
from app import app
from app.models.user import User
from app.models.base import db
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *


'''To return a list of all users as a JSON object'''
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

@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def modify_user(user_id):
  user = User.get(User.id == user_id)

  if request.method == "GET":
      if user:
          return jsonify(user.to_hash())
      else:
          return jsonify(msg="User does not exist."), 404


      if user:
          return jsonify(user.to_hash())




  elif request.method == 'PUT':

      user_info = request.values
      for key in user_info:
          '''Sustained by MySQL'''
          if key == 'updated_at' or key == 'created_at' or key == 'id':
              continue
          if key == 'first_name':
              user.first_name = user_info.get(key)
          if key == 'last_name':
              user.last_name = user_info.get(key)
          if key == 'email' or key == 'is_admin':
              return jsonify(msg="This one cannot be changed")
          if key == 'password':
              user.password = user_info.get(key)

      user.save()
      return jsonify(user.to_hash())

  elif request.method == 'DELETE':
      user_info = User.get(User.id == user_id)
      user_info.delete_instance()
      user_info.save()
      return jsonify(msg="User deleted")
