from django.contrib import admin
# We add the django model to the admin so that we see it along side other models
from .models import Todo
# Register the model
admin.site.register(Todo)