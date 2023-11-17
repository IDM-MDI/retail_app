from django.db import models

from electronics_retail.models.address import Address


class Contact(models.Model):
    email = models.EmailField(max_length=255)
    address = models.OneToOneField(to=Address, on_delete=models.CASCADE, primary_key=True)
