from django.contrib import admin

# Register your models here.
from weddingmanager.theme.models import DecorItem, Item, Theme

admin.site.register(Theme)
admin.site.register(DecorItem)
admin.site.register(Item)
