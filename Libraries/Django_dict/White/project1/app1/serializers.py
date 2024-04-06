from rest_framework.serializers import ModelSerializer
from app1.models import SalesOrder

class OrderSerializer(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description']

        