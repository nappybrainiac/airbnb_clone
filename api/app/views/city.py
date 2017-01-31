from app import app
from app.models.state import State
from app.models.city import City
from app.models.base import db
from flask import request, jsonify, json
from peewee import *
import flask


@app.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def get_post_cities(state_id):
    if request.method == 'GET':
        city_list = City.select().where(City.state == state_id)
        order_values = [i.to_hash() for i in city_list]
        return jsonify(order_values)

    elif request.method == 'POST':

        check_city_name = City.select().where(City.name == request.form['name']).where(City.state == state_id)

        if check_city_name:
            error_msg = {
                'code': 10002,
                'msg': 'City already exists in this state'
            }
            return jsonify(error_msg), 409

        else:
            city = City.create(
                name = request.form['name'],
                state = state_id
            )
        return jsonify(city.to_hash())

@app.route('/states/<state_id>/cities/<city_id>', methods=['GET', 'DELETE'])
def view_modify_cities(state_id, city_id):
    if request.method == 'GET':
        city_list = City.select().where(City.id == city_id).where(City.state == state_id)
        order_values = [i.to_hash() for i in city_list]
        return jsonify(order_values)

    elif request.method == 'DELETE':
        city_info = City.select().where(City.id == city_id).where(City.state == state_id).first()
        city_info.delete_instance()
        city_info.save()
        delete_msg = {'msg':'City has been deleted'}
        return jsonify(delete_msg)