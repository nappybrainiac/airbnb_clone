from peewee import *
from base import * # in order to use BaseModel
from hashlib import md5 # for md5 hashing

'''Create the User table'''
class User(BaseModel):
    email = CharField(128, null = False, unique = False)
    password = CharField(128, null = False)
    first_name = CharField(128, null = False)
    last_name = CharField(128, null = False)
    is_admin = BooleanField(default = False)

    def set_password(self, clear_password):
        #using md5 hash algorithm to secure the password
        password = md5.new(clear_password.encode).digest()

    '''Convert the table into hash information'''
    def to_hash(self):
        info = {
                'id': self.id,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'is_admin': self.is_admin
                }
        return info
