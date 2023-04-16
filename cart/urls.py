from django.urls import path,include
from cart.views import get_all_Product_in_Cart,addToCart,delete_Oneproduct_Incart,total_of_price,quantity_increase,quantity_decrease


urlpatterns = [
     path('',get_all_Product_in_Cart,name='all_product_in_Cart'),
     path('add/',addToCart,name='add_product_in_cart'),
     path('delete/<int:id>',delete_Oneproduct_Incart,name='delete_one'),
     path('total/',total_of_price,name='total_price'),
     path('quantity_increase/<int:id>/',quantity_increase,name='increase_quantity'),
     path('quantity_decrease/<int:id>/',quantity_decrease,name='decrease_quantity'),
   
]