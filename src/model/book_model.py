from mongoengine import *


class Book(Document):
    title = StringField(max_length=200, required=True)
    price = FloatField()
    description = StringField()
    author = StringField(max_length=50, required=True)
