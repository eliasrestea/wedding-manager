from django.db import models

# Create your models here.


class Service(models.Model):
    slug = models.SlugField(max_length=50)
    service_price = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    service_file = models.ImageField(null=True)

    def __str__(self):
        return self.slug


class Venue(models.Model):
    slug = models.SlugField()
    services = models.ManyToManyField(Service)
    description = models.CharField(max_length=500, null=True)
    capacity = models.IntegerField()
    surface_area = models.IntegerField()
    parking_spaces = models.IntegerField()
    venue_price = models.IntegerField(null=True)
    venue_file = models.ImageField(null=True)
    # available =

    def __str__(self):
        return self.slug
