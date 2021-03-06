# Imports
from config import *
from peewee import *
import os
import datetime
import sys
import peewee


# Creating an instance of a database
db = MySQLDatabase(
    database = DATABASE["database"],
    host = DATABASE["host"],
    user = DATABASE["user"],
    port = DATABASE["port"],
    passwd = DATABASE["password"],
    charset = DATABASE["charset"])

# Base model for the classes
class BaseModel(peewee.Model):
    id = PrimaryKeyField(primary_key = True, unique = True)
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)


    class Meta:
        database = db
        order_by = ("id", )
