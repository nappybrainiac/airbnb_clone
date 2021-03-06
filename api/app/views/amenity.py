'''
Project:    AirBnB Clone
File:       amenity.py
By:         Mackenzie Adams, Gloria Bwandungi

This file contains the route() decorator to tell Flask what URL
should trigger our functions and determine how amenities are viewed
added, and modified in the database.
'''

import flask
from app import app
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *


'''This function returns JSON lists using GET and POST methods.
   It lists all the amenities using the GET method, or creates
   a new one using the POST method'''
@app.route('/amenities', methods=['GET', 'POST'])
def amenity_create():
    if request.method == 'GET':
        amenity_list = Amenity.select()

        '''If there are no amenities, return an error message.'''
        if amenity_list:
            order_values = [i.to_hash() for i in amenity_list]
            return jsonify(order_values)

        else:
            return jsonify(msg="No records to display"), 404


    elif request.method == 'POST':
        '''If the amenity name already exists, return an error message.'''
        amenity_check = Amenity.select().where(Amenity.name == request.form['name']).first()

        if amenity_check:
            return jsonify(code=10003, msg="Name already exists"), 409

        else:
            amenity_info = Amenity.create(
                name = request.form['name']
            )
            return jsonify(amenity_info.to_hash())

'''This function returns JSON lists using GET and POST methods.
   It lists a the amenities by amenity_id using the
   GET method, or creates a new one using the POST method'''
@app.route('/amenities/<amenity_id>', methods=['GET', 'DELETE'])
def modify_amenity(amenity_id):
    amenity = Amenity.get(Amenity.id == amenity_id)

    if request.method == "GET":
        if amenity:
            return jsonify(amenity.to_hash())
        else:
            return jsonify(msg="This id does not exist."), 404

    elif request.method == 'DELETE':
      amenity_info = Amenity.select().where(Amenity.id == amenity_id).first()
      amenity_info.delete_instance()
      amenity_info.save()
      return jsonify(msg="Amenity deleted")

'''This function returns JSON lists using GET method.
   It lists a the amenities in a place by place_id using the
   GET method.'''
@app.route('/places/<place_id>/amenities', methods=['GET'])
def place_amenity(place_id):
    amenity_place = PlaceAmenities.get(PlaceAmenities.place == place_id)
    return jsonify(amenity_info.to_hash())
