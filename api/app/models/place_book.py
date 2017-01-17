import peewee
import base
from place import place
from user import User

class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name='places_booked')
    is_validated = BooleanField(default=False)
    date_start = DateTimeField(default=datetime.datetime.now(), null=False)
