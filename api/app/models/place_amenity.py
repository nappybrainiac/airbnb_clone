import peewee
from base import BaseModel, db
from place import Place
from amenity import Amenity
from peewee import *

'''Create the PlaceAmenities table'''
class PlaceAmenities(peewee.Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta:
        database = db
