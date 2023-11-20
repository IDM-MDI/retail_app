from django.db import models
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from electronics_retail.models import Retail
from electronics_retail.serializers.retail_serializer import RetailSerializer


class RetailHighDebtAVG(generics.ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        average_debt = Retail.objects.aggregate(avg_debt=models.Avg('debt'))['avg_debt']
        return Retail.objects.filter(debt__gt=average_debt)
