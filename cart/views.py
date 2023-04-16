from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from product.models import Product
from cart.serializers import CartSerializer,CreateCartSerializer
from django.db.models import Sum
# Create your views here.


@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def get_all_Product_in_Cart(request):
    if request.method == "GET":   
       queryset = Cart.objects.filter(user = request.user.id).select_related('product')
       serializer = CartSerializer(queryset, many = True)
       return Response(serializer.data)
    if request.method == "DELETE":   
       Cart.objects.filter(user = request.user.id).select_related('product').delete()
       return Response({"message":'deleted'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToCart(request):
    if request.method == "POST":     
       cart = Cart.objects.filter(product = request.data.get('product'),user = request.user.id)
       get_product = Product.objects.filter(id = request.data.get('product'))
       print(get_product)
       if get_product:
          if not cart:
            serializer = CreateCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user = request.user,tprice=get_product[0].price)
                return Response(serializer.data, status=status.HTTP_201_CREATED)     
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          elif cart:
             serializer = CartSerializer(cart, many = True)
             cart[0].quantity +=1
             cart[0].tprice +=get_product[0].price
             cart[0].save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)     
       elif not get_product:
            not_found = {'message': 'Not found'}
            return Response(not_found,status=status.HTTP_404_NOT_FOUND)    
              
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_Oneproduct_Incart(request,id):
      cart = Cart.objects.filter(product = id,user = request.user.id)
      print(cart)
      if(cart):
         cart.delete()
         return Response({'message':'Product in Cart deleted'})
      else:
         not_found = {'message': 'Not found'}
         return Response(not_found,status=status.HTTP_404_NOT_FOUND)    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_of_price(request):
    cart = Cart.objects.filter(user = request.user.id).aggregate(Sum("tprice"))
    return Response(cart)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def quantity_increase(request,id):
    cart = Cart.objects.filter(user = request.user.id,product = id)
    get_product = Product.objects.filter(id = id)
    if cart:
       serializer = CartSerializer(cart, many = True)
       cart[0].quantity += 1
       cart[0].tprice += get_product[0].price
       cart[0].save()
       return Response(serializer.data)
    else:
      not_found = {'message': 'Not found'}
      return Response(not_found,status=status.HTTP_404_NOT_FOUND)
    


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def quantity_decrease(request,id):
    cart = Cart.objects.filter(user = request.user.id,product = id)
    get_product = Product.objects.filter(id = id)
    if cart:
       serializer = CartSerializer(cart, many = True)
       cart[0].quantity -= 1
       cart[0].tprice -= get_product[0].price
       cart[0].save()
       return Response(serializer.data)
    else:
      not_found = {'message': 'Not found'}
      return Response(not_found,status=status.HTTP_404_NOT_FOUND)
    
