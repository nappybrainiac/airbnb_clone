import peewee
import base


class Amenity(BaseModel):
    name = CharField(128, null=False)
