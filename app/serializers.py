from rest_framework import serializers
from .models import CartItem

class CartSerializer(serializers.ModelSerializer):
 productname=serializers.CharField(max_length=100)
 productprice=serializers.IntegerField()
 productquantity=serializers.IntegerField()

 class Meta:
    Model=CartItem
    fields='__all__'
    