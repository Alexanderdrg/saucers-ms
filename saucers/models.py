from django.db import models


# Create your models here.
class Saucer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    ingredients = models.ManyToManyField
    additional = models.ManyToManyField
    price = models.FloatField(null=True, blank=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class Additional(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
