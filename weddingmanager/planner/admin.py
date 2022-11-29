from django.contrib import admin

from .models import Order, Services, Venue

# Register your models here.

admin.site.register(Order)
admin.site.register(Venue)
admin.site.register(Services)
