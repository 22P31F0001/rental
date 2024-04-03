from django.contrib import admin

# Register your models here.
from .models import bikecategory,bikedata

admin.site.register(bikecategory)
admin.site.register(bikedata)