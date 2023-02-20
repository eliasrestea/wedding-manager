from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DecorItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name
