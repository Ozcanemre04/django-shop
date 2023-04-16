from django.test import TestCase
from product.views import get_all_Product,get_one_Product
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from rest_framework.test import APITestCase,APIRequestFactory
from product.models import Product
from product.serializers import ProductSerializer

class ApiUrlsTests(APITestCase):

    databases = '__all__'

    def setUp(self):
        self.product = Product.objects.create(
                  title= "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                  price= 109.95,
                  description= "Your perfect pack for everyday use and walks in the forest.Stash your laptop",
                  category= "men's clothing",
                  image= "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg", 
                  rate= 3.9,
                  count= 120,)
        self.product.save()


    def test_all_product_url(self):
        url = reverse('all_product')
        self.assertEqual(resolve(url).func,get_all_Product)
        response = self.client.get('/api/product/all/')
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data,serializer.data)
    

    def test_one_product_url(self):
        url = reverse('one_product',kwargs={'id':2})
        self.assertEqual(resolve(url).func,get_one_Product)

        response = self.client.get('/api/product/3/',format='json')
        if response.data != {'message':'not found'}:
           product = Product.objects.filter(id=3)
           serializer = ProductSerializer(product,many=True)
           print(response.data)
           print(serializer.data)
           self.assertEqual(len(response.data),1)
           self.assertEqual(Product.objects.get().id,3)
           self.assertEqual(response.data,serializer.data)
        else:
            print('not found')

    def test_one_product_Not_found(self):
        response = self.client.get('/api/product/100/',format='json')
        self.assertEqual(response.data,{'message':'not found'})

        

