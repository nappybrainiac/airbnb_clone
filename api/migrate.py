import peewee
from user import user
from state import state
from city import city
from place import Place
from place_book import PlaceBook
from amenity import Amenity
from place_amenity import PlaceAmenities 

def create_tables():
    database.connect()
    database.create_tables([User, State, City, Place, PlaceBook, Amenity, PlaceAmenities])
