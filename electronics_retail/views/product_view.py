from rest_framework import viewsets

from electronics_retail.models import Product
from electronics_retail.serializers import ProductSerializer


class ProductModelView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


