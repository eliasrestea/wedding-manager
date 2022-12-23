from django.db import models

from weddingmanager.venues.models import Service, Venue

# Create your models here.


class Order(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    chosen_services = models.ManyToManyField(Service, null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    # date =
