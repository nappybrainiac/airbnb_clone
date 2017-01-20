import peewee
import base

'''Create the State table'''
class State(BaseModel):
    name = CharField(128, null=False, unique=True)

    '''Convert the table into hash information'''
    def to_hash(self):
        info = {
                'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'name': self.name
                }
        return info
