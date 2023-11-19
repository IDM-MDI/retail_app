from rest_framework import viewsets

from electronics_retail.models import Retail
from electronics_retail.serializers.retail_serializer import RetailSerializer


class RetailModelSet(viewsets.ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
