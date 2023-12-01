from django.db.models.signals import post_save
from django.dispatch import receiver

from electronics_retail.models import Retail
from electronics_retail.service import send_email


@receiver(post_save, sender=Retail)
def post_retail(instance, **kwargs):
    send_email(list(instance.users.values_list('email', flat=True)), instance.contact)