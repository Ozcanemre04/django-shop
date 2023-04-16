from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def get_product_api(request):
    url = f'https://fakestoreapi.com/products'
    res = requests.get(url).json()
    return Response(res)


@api_view(['GET'])
def get_all_Product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_Product(request,id):
    product = Product.objects.filter(id = id)
    serializer = ProductSerializer(product, many = True)
    not_found = {'message': 'not found'}
    if(len(product)> 0):
       return Response(serializer.data)
    else:
        return Response(not_found,status=status.HTTP_404_NOT_FOUND)