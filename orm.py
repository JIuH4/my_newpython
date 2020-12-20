from datetime import date

from peewee import SqliteDatabase, Model, DateField, CharField, BooleanField, IntegerField, ForeignKeyField

db = SqliteDatabase("people.db")


class Person(Model):
    name = CharField()
    date_of_birth = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    name = CharField()
    owner = ForeignKeyField(Person, related_name="pets")
    animal_tipe = CharField

    class Meta:
        database = db

bob= Person.select().where(Person.name=="Bob").get()

# Pet.create(name="Lucy",animal_tipe="cat",owner=bob.id)

print(list(bob.pets)[0].name)

bob.delete_instance()