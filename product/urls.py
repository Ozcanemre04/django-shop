from django.urls import path,include
from product.views import get_product_api,get_all_Product,get_one_Product

urlpatterns = [

     path('',get_product_api,name='all_product_api'),
     path('all/',get_all_Product,name='all_product'),
     path('<int:id>/',get_one_Product,name='one_product'),
]