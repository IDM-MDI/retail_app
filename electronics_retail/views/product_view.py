from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from electronics_retail.models import Product
from electronics_retail.serializers import ProductSerializer


class ProductModelView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )


