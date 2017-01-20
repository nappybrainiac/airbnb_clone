import peewee
import base

'''The Amenity table'''
class Amenity(BaseModel):
    name = CharField(128, null=False)

    '''To return hash of table attributes'''
    def to_hash(self):
        info = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name
        }
        return info
