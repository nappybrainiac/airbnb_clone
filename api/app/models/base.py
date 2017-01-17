# Imports
import config
import peewee
import os

# Creating an instance of a database
database = connect(os.environ.get('DATABASE')

# Base model for the database
class BaseModel(peewee.Model):
    id = PrimaryKeyField(primary_key = True, unique = True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()

    class Meta:
        database = database
        order_by = ("id", )
