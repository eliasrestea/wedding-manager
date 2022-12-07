from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    slug = models.SlugField()
    services = models.ManyToManyField(Service)
    description = models.CharField(max_length=500, null=True)
    capacity = models.IntegerField()
    surface_area = models.IntegerField()
    parking_spaces = models.IntegerField()
    venue_price = models.FloatField(null=True)
    # available =

    def __str__(self):
        return self.slug


class Order(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    chosen_services = models.ManyToManyField(Service, null=True)
    total_price = models.FloatField(null=True)
    # date =
