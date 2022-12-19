from django.contrib import admin

from .models import File, Order, Service, Venue

# Register your models here.

admin.site.register(Order)
admin.site.register(Venue)
admin.site.register(Service)
admin.site.register(File)
