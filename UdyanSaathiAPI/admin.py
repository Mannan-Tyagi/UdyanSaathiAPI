from django.contrib import admin
from .models import pollutionModel  # Import the model class

# Register the model class with the admin site
admin.site.register([pollutionModel])  # Use square brackets to create an iterable with the model class
