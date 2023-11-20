from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'email': {'required': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)