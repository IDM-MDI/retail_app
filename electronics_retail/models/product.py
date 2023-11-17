from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    release = models.DateField()
