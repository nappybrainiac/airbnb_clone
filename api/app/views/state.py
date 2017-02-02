'''
Project:    AirBnB Clone
File:       state.py
By:         Mackenzie Adams, Gloria Bwandungi

This file contains the app decorators that determine how states are viewed
added, and modified in the database.
'''


from app import app
from app.models.state import State
from app.models.base import db
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *
import flask


'''This function returns JSON lists using GET and POST methods.
   It lists all the states using the GET method, or creates
   a new one using the POST method'''
@app.route('/states', methods=['GET', 'POST'])
def state_create_modify():
    if request.method == 'GET':
        state_list = State.select()
        order_values = [i.to_hash() for i in state_list]
        return jsonify(order_values)

    elif request.method == 'POST':

        check_state_name = State.select().where(State.name == request.form['name'])

        if check_state_name:
            error_msg = {
                'code': 10001,
                'msg': 'State already exists'
            }
            return jsonify(error_msg)

        else:
            state = State.create(
                name = request.form['name']
            )
        return jsonify(state.to_hash())

'''This function returns JSON lists using GET and POST methods.
   It lists a the state by state_id using the
   GET method, or creates a new one using the POST method'''
@app.route('/states/<state_id>', methods=['GET','DELETE'])
def modify_state(state_id):
  state = State.get(State.id == state_id)

  if request.method == "GET":
      return jsonify(state.to_hash())


  elif request.method == 'DELETE':
      state_info = State.get(State.id == state_id)
      state_info.delete_instance()
      state_info.save()
      return jsonify(msg="State deleted")
