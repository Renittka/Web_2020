from django.db import models


class Product(models.Model):
    name = models.CharField()
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()


class Category(models.Model):
    name = models.CharField()
