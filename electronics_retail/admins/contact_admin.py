from django.contrib import admin

from electronics_retail.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
