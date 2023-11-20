from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from electronics_retail.models import Retail
from electronics_retail.permissions import IsAdminOrOwnerReadOnly
from electronics_retail.serializers import RetailSerializer


class RetailModelView(viewsets.ModelViewSet):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('contact__address__city', 'product__id', )
    permission_classes = [IsAdminOrOwnerReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Retail.objects.all() if user.is_staff else Retail.objects.filter(users=user)
