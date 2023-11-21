import random

from retail_app.celery import app
from electronics_retail.models import Retail


@app.task
def increase_debt():
    retailers = Retail.objects.all()
    for retail in retailers:
        random_increase = random.randint(5, 500)
        retail.debt += random_increase
        retail.save()


@app.task
def decrease_debt():
    retailers = Retail.objects.all()
    for retail in retailers:
        random_decrease = random.randint(100, 10000)
        new_debt = retail.debt - random_decrease
        retail.debt = max(new_debt, 0)
        retail.save()


@app.task
def clear_debt_async(queryset):
    print(queryset)
    return queryset.update(debt=0)

