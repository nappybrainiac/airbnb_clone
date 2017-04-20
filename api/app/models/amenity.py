from peewee import *
from base import BaseModel

'''The Amenity table'''
class Amenity(BaseModel):
    name = CharField(128, null=False)

    '''To return hash of table attributes'''
    def to_hash(self):
        info = {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y/%m/%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y/%m/%d %H:%M:%S'),
            'name': self.name
        }
        return info
