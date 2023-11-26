from django.contrib import admin

from electronics_retail.models import Retail, RetailType
from electronics_retail.service.debt_service import clear_debt_async


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_filter = ('contact__address__city',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.type == RetailType.FACTORY:
            form.base_fields['provider'].queryset = Retail.objects.none()
        return form

    @admin.action(description="Clear selected elements' debt")
    def clear_debt(self, request, queryset):
        return queryset.update(debt=0) if len(queryset) < 20 else clear_debt_async(queryset)

    actions = (clear_debt,)
