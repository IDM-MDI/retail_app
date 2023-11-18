from django import forms
from django.contrib import admin

from electronics_retail.models import Retail, Product, Contact, Address, RetailType


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.type == RetailType.FACTORY:
            form.base_fields['provider'].queryset = Retail.objects.none()
        return form


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
