from django.contrib import admin

from electronics_retail.models import Retail, RetailType


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
        print(queryset)
        queryset.update(debt=0)
        return queryset

    actions = (clear_debt,)
