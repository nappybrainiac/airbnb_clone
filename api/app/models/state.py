import peewee
import base

class State(BaseModel):
    name = CharField(128, null=False, unique=True)