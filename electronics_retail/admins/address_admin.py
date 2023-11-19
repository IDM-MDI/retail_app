from django.contrib import admin

from electronics_retail.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
