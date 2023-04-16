from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    image = models.URLField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    count = models.PositiveBigIntegerField()
    def __str__(self):
        return f"{self.id} {self.title}"
    
