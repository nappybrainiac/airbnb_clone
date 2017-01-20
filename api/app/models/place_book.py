import peewee
import base
from place import place
from user import User

'''Create the PlaceBook table'''
class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name='places_booked')
    is_validated = BooleanField(default=False)
    date_start = DateTimeField(default=datetime.datetime.now(), null=False)
    number_nights = IntegerField(default=1)

    '''Convert table information into hash information'''
    def to_hash(self):
        info = {
                'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'place_id': self.place,
                'user_id': self.user,
                'is_validated': self.is_validated,
                'date_start': self.date_start,
                'number_nights': self.number_nights
                }
        return info
