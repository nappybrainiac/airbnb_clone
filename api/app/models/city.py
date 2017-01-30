from peewee import *
from base import BaseModel
from state import State

'''Create the table City'''
class City(BaseModel):
    name = CharField(128, null=False)
    state = ForeignKeyField(State, related_name='cities')

    '''Convert table information into hash information'''
    def to_hash(self):
        info = {
                'id': self.id,
                'created_at': self.created_at.strftime('%Y/%m/%d %H:%M:%S'),
                'updated_at': self.updated_at.strftime('%Y/%m/%d %H:%M:%S'),
                'name': self.name,
                'state_id': self.state_id
                }
        return info
