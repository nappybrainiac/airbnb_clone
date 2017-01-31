import flask
from app import app
from app.models.place import Place
from app.models.user import User
from app.models.city import City
from app.models.state import State
from app.models.base import db
from flask import request, jsonify, json
from flask_json import json_response
from peewee import *


@app.route('/places', methods = ['GET', 'POST'])
def list_post_places():
    if request.method == 'GET':
        places_list = Place.select()
        order_values = [i.to_hash() for i in places_list]
        return jsonify(order_values)

    elif request.method == 'POST':
        place_info = Place.create(
            owner_id=request.form['owner_id'],
            city_id=request.form['city_id'],
            name=request.form['name'],
            description=request.form['description'],
            number_rooms=request.form['number_rooms'],
            number_bathrooms=request.form['number_bathrooms'],
            max_guest=request.form['max_guest'],
            price_by_night=request.form['price_by_night'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
        )
        return jsonify(place_info.to_hash())

@app.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def list_put_delete():
    place = Place.get().where(Place.id == place_id)

    if method == 'GET':
        return jsonify(place.to_hash())

    elif method =='PUT':
        place_info = request.values
        for key in place_info:
            '''Sustained by MySQL'''
            if key == 'updated_at' or key == 'created_at' or key == 'id':
                continue
            if key == 'owner_id':
                place.owner_id = place_info.get(key)
            if key == 'city_id':
                place.city_id = place_info.get(key)
            if key == 'name':
                place.name = place_info.get(key)
            if key == 'description':
                place.description = place_info.get(key)
            if key == 'number_rooms':
                place.number_rooms = place_info.get(key)
            if key == 'number_bathrooms':
                place.number_bathrooms = place_info.get(key)
            if key == 'max_guest':
                place.max_guest = place_info.get(key)
            if key == 'price_by_night':
                place.price_by_night = place_info.get(key)
            if key == 'latitude':
                place.latitude = place_info.get(key)
            if key == 'longitude':
                place.longitude = place_info.get(key)

        user.save()
        return jsonify(place.to_hash())

    elif method == 'DELETE':
        place_info = Place.get().where(Place.id == place_id)
        place_info.delete_instance()
        place_info.save()
        return jsonify(msg='Place deleted')

'''View and/or create a place using state_id and city_id'''
@app.route('/states/<state_id>/cities/<city_id>/places', methods=['GET', 'POST'])
def list_place_by_state():
    place_info = Place.get().where(Place.state == state_id).where(Place.city == city_id)

    if method == 'GET':
            jsonify(place_info.to_hash())

    elif method == 'POST':
        place_info = Place.create(
            owner_id=request.form['owner_id'],
            city_id=request.form['city_id'],
            name=request.form['name'],
            description=request.form['description'],
            number_rooms=request.form['number_rooms'],
            number_bathrooms=request.form['number_bathrooms'],
            max_guest=request.form['max_guest'],
            price_by_night=request.form['price_by_night'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude']
        )
        return jsonify(place_info.to_hash())
