from django.contrib import admin

from electronics_retail.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
