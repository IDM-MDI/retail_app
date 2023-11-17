from django.contrib import admin

from electronics_retail.models import Retail, Product


@admin.register(Retail)
class AdminRetail(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
