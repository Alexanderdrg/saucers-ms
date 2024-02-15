from django.db import models


# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Additional(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Saucer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    additional = models.ManyToManyField(Additional)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
