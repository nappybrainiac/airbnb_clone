from peewee import *
from base import BaseModel


'''Create the State table'''
class State(BaseModel):
    name = CharField(128, null=False, unique=True)

    '''Convert the table into hash information'''
    def to_hash(self):
        info = {
                'id': self.id,
                'created_at': self.created_at.strftime('%Y/%m/%d %H:%M:%S'),
                'updated_at': self.updated_at.strftime('%Y/%m/%d %H:%M:%S'),
                'name': self.name
                }
        return info
