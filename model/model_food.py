mport sqlite3
from peewee import *


#create reference to SQLite database file
db = SqliteDatabase("database/food.db")

"""represents an artist in the database
    """
class Food(Model):
    id = AutoField()
    food_name = CharField(unique=True)
    recipe_instructions = CharField(unique=True)
    recipe_ingredients =  CharField(unique=True)
    drink_name = CharField(unique=True)
    drink_ingredients = CharField(unique=True)
    img_file_name = CharField(unique=True)

    class Meta():
        database = db #this model uses the "arts.db" database
        constraints = [SQL('UNIQUE( name COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: {self.name}: {self.recipe_instructions}: 
        {self.recipe_ingredients}: {self.drink_name}: {self.drink_ingredients}: {self.img}'



db.connect()
db.create_tables([Food])