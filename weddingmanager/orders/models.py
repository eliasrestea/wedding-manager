from django.contrib.auth import get_user_model
from django.db import models

from weddingmanager.theme.models import DecorItem
from weddingmanager.venues.models import Service, Venue

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    chosen_services = models.ManyToManyField(Service, null=True, blank=True)
    chosen_decor_items = models.ManyToManyField(DecorItem, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    date = models.CharField(null=True, blank=True, max_length=10)
