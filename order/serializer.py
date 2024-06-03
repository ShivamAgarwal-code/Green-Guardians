from rest_framework import serializers
from .models import CartOrder

class CartOrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartOrder
    fields = '__all__'