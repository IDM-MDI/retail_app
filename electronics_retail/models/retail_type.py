from django.db import models
from django.utils.translation import gettext_lazy as _


class RetailType(models.TextChoices):
    FACTORY = 'FC', _('Factory')
    DISTRIBUTOR = 'DB', _('Distributor')
    DEALER = 'DL', _('Dealer')
    LARGE_RETAIL = 'LR', _('Large Retail')
    ENTREPRENEUR = 'IE', _('Individual Entrepreneur')