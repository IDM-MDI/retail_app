from rest_framework import serializers

from electronics_retail.models import Retail


class RetailSerializer(serializers.ModelSerializer):
    class Meta:
        model: Retail
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
