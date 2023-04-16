from django.test import TestCase
from rest_framework.test import APITestCase,APIClient
from django.urls import reverse,resolve
from rest_framework import status
from product.models import Product
from cart.models import Cart
from accounts.models import account
import json
from django.db.models import Sum

from cart.serializers import CartSerializer

class CartTest(APITestCase):
    databases = '__all__'

    def setUp(self):
        self.user = account.objects.create(
            email= "foo@fo.com",
            username= "emre",
            password= "emre",
            first_name= "foo",
            last_name= "bar"
        )
        self.user.save()

        self.product = Product.objects.create(
                  id = 1,
                  title= "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                  price= 100.00,
                  description= "Your perfect pack for everyday use and walks in the forest.Stash your laptop",
                  category= "men's clothing",
                  image= "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg", 
                  rate= 3.9,
                  count= 120,)

        self.product = Product.objects.create(
                  id = 2,
                  title= "Fjallraven - Foldsack No. 1 Backpack, Fits 200 Laptops",
                  price= 50.50,
                  description= "Your perfect pack for everyday use and walks in the forest.Stash your laptop",
                  category= "men's clothing",
                  image= "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg", 
                  rate= 3.9,
                  count= 120,)
        
        self.client = APIClient()
        user = account.objects.get(username='emre')
        self.client.force_authenticate(user=user)
        url = reverse('add_product_in_cart')
        print(Product.objects.get(id=2))
        self.product = Product.objects.get(id=2)
        data ={ "product":self.product.id}
        self.client.post(url,data,format='json')
        self.client.post(url,data,format='json')


        

    def test_Delete_One(self):
        self.assertEqual(len(Cart.objects.all()),1)
        response = self.client.delete('/api/cart/delete/2')
        if response == {'message':'Product in Cart deleted'}:
          self.assertEqual((Cart.objects.count()),0)

    def test_Delete_One_not_found(self):
        response = self.client.delete('/api/cart/delete/200')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'message':'Not found'})



    def test_all_Cart_and_delete(self):
        url = reverse('all_product_in_Cart')
        response = self.client.get(url)
        self.assertEqual(len(response.data),1)
        response = self.client.delete(url)
        self.assertEqual(len(Cart.objects.all()),0)

    def testCartadd(self):
        self.assertEqual(Cart.objects.count(), 1)
        url = reverse('add_product_in_cart')
        data ={
            "product":Product.objects.get(id=1).id
        }
        self.client.post(url,data,format='json')
        response =self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 2)
        self.assertEqual(Cart.objects.filter(id=1)[0].id, 1)
        dumps = json.dumps(response.data[0])
        loads = json.loads(dumps)
        cart = Cart.objects.filter(product=1)
        serializer = CartSerializer(cart,many=True)
        self.assertEqual(loads['tprice'], '200.00')
        self.assertEqual(loads['quantity'], 2)
        self.assertEqual(response.data, serializer.data)
        
       


    def test_total_price(self):
        url = reverse('total_price')
        response= self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tprice__sum'].__str__(), '101.00')



    def test_quantity_increase(self):
       self.assertEqual(Cart.objects.filter(product=2)[0].quantity, 2)
       response= self.client.patch('/api/cart/quantity_increase/2/',format='json')
       if response.status_code == 200:
          cart = Cart.objects.filter(product=2)
          serializer = CartSerializer(cart,many=True)
          dumps = json.dumps(response.data[0])
          loads = json.loads(dumps)

          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data, serializer.data)
          self.assertEqual(loads['quantity'], cart[0].quantity)
          self.assertEqual(loads['quantity'], 3)
          self.assertEqual(Cart.objects.filter(product=2)[0].quantity, 3)
          self.assertEqual(loads['tprice'], cart[0].tprice.__str__())


    def test_quantity_decrease(self):
       self.assertEqual(Cart.objects.filter(product=2)[0].quantity, 2)
       response= self.client.patch('/api/cart/quantity_decrease/2/',format='json')
       if response.status_code == 200:
          cart = Cart.objects.filter(product=2)
          serializer = CartSerializer(cart,many=True)
          dumps = json.dumps(response.data[0])
          loads = json.loads(dumps)
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data, serializer.data)
          self.assertEqual(loads['quantity'], cart[0].quantity)
          self.assertEqual(loads['quantity'], 1)
          self.assertEqual(loads['tprice'], cart[0].tprice.__str__())





    def test_quantity_increase_not_found(self):
       response= self.client.patch('/api/cart/quantity_increase/123/',format='json')
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_quantity_decrease_not_found(self):
       response= self.client.patch('/api/cart/quantity_decrease/123/',format='json')
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       
        


  





