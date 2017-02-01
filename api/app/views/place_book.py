from app import app
from app.models.place import Place
from app.models.place_book import PlaceBook
from flask import request, jsonify, json
from peewee import *



'''View and create all bookings to a particular place identified by place_id.'''
@app.route('/places/<place_id>/books', methods=['GET', 'POST'])
def view_create_placebook(place_id):
    if request.method == 'GET':
        place = PlaceBook.select().where(PlaceBook.place == place_id)

        if place:
            order_values = [i.to_hash() for i in place]
            return jsonify(order_values)

        else:
            return jsonify(msg="There are no bookings for this place."), 404    

    elif request.method == 'POST':
        place = PlaceBook.create(
            place = place_id,
            user = request.form['user'],
            is_validated = request.form['is_validated'],
            date_start = request.form['date_start'],
            number_nights = request.form['number_nights']
        )
        return jsonify(place.to_hash())

'''View, create, and delete bookings using the place_id to identify them.'''
@app.route('/places/<place_id>/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def view_create_delete(place_id, book_id):
    bookings = PlaceBook.select().where(PlaceBook.place == place_id).where(PlaceBook.id == book_id).first()

    if request.method == 'GET':
        return jsonify(bookings.to_hash())

    elif request.method == 'PUT':
        booking_info = request.values
        for key in booking_info:
            '''Sustained by MySQL'''
            if key == 'place':
                bookings.place = booking_info.get(key)
            if key == 'user':
                return jsonify(msg="User cannot be changed")
            if key == 'is_validated':
                bookings.is_validated = booking_info.get(key)
            if key == 'date_start':
                bookings.date_start = booking_info.get(key)
            if key == 'number_nights':
                bookings.number_nights = booking_info.get(key)

        bookings.save()
        return jsonify(bookings.to_hash())

    elif request.method == 'DELETE':
        booking_info = PlaceBook.select().where(PlaceBook.place == place_id).where(PlaceBook.id == book_id).first()
        booking_info.delete_instance()
        place_info.save()
        return jsonify(msg='Booking deleted')
