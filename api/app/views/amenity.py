import flask
from app import app
from app.models.amenity import Amenity
from app.models.base import db
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *


'''To return a list of all users as a JSON object'''
@app.route('/amenities', methods=['GET', 'POST'])
def amenity_create():
    if request.method == 'GET':
        amenity_list = Amenity.select()
        order_values = [i.to_hash() for i in amenity_list]
        return jsonify(order_values)

    elif request.method == 'POST':
        amenity_info = Amenity.create(
            name = request.form['name']
        )
        return jsonify(amenity_info.to_hash())

@app.route('/amenities/<amenity_id>', methods=['GET', 'DELETE'])
def modify_amenity(amenity_id):
  amenity = Amenity.get(Amenity.id == amenity_id)

  if request.method == "GET":
      return jsonify(amenity.to_hash())

  elif request.method == 'DELETE':
      amenity_info = Amenity.select().where(Amenity.id == amenity_id).first()
      amenity_info.delete_instance()
      amenity_info.save()
      return jsonify(msg="Amenity deleted")
