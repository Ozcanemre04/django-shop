from rest_framework import serializers
from .models import Cart
from product.models import Product
from product.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','quantity','user_id','tprice','product')
        depth = 1

class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user','tprice','product','quantity')
        read_only_fields = ("user","tprice",'quantity')


  
