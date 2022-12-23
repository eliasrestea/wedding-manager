from django.contrib import admin

from .models import Service, Venue

# Register your models here.

admin.site.register(Venue)
admin.site.register(Service)
