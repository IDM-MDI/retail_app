from rest_framework import serializers

from electronics_retail.models import Retail


class RetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Retail
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            del validated_data['debt']

        return super().update(instance, validated_data)
