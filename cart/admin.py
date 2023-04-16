from django.contrib import admin
from cart.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product']
    list_filter= ('user',)
    

admin.site.register(Cart,CartAdmin)