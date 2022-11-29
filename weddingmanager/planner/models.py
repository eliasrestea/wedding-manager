from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)
    # employees =

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=50)
    services = models.ManyToManyField(Services)
    description = models.CharField(max_length=500, null=True)
    capacity = models.FloatField()
    # available =

    def __str__(self):
        return self.name


class Order(models.Model):
    venue = models.ForeignKey(Venue, null=True, on_delete=models.SET_NULL)
    services = models.ManyToManyField(Services, null=True)
    # date =
