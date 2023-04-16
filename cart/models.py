from django.db import models
from accounts.models import account
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user= models.ForeignKey(account,on_delete=models.CASCADE,related_name='Cart_user')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Cart_product')
    quantity = models.PositiveIntegerField(default=1)
    tprice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
          unique_together = ('user','product',)

    def __str__(self):
        return f"{self.user} {self.product} {self.quantity} {self.tprice}"