import peewee
import base
from state import State

class City(BaseModel):
    name = CharField(128, null=False)
    state = ForeignKeyField(State, related_name='cities')
