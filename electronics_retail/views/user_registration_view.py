from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from electronics_retail.serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

