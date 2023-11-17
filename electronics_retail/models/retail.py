from django.contrib.auth.models import User
from django.db import models

from electronics_retail.models.contact import Contact
from electronics_retail.models.product import Product
from electronics_retail.models.retail_type import RetailType


class Retail(models.Model):
    name = models.CharField(max_length=255)
    contact = models.OneToOneField(to=Contact, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product)
    users = models.ManyToManyField(to=User)
    debt = models.DecimalField()
    type = models.CharField(
        max_length=2,
        choices=RetailType.choices,
    )
    create_time = models.DateTimeField(auto_now_add=True)