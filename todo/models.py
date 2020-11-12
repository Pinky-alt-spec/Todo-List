from django.db import models

# model - a representation of data we want to store in the database

# The model will inherit from django's model' - models.Model
class Todo(models.Model):
    # A sequel table with a column called name and restriction on the length of the string is 100
    # And a column called due_date with data type is a date object
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    # To apply the schema to our database we use 2 commands
            # python manage.py makemigrations
            # python manage.py migrate
    #use the same name from input
    def __str__(self):
        return self.name
