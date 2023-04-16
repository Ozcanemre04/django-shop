from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class account(AbstractUser):
    email = models.EmailField(unique=True,max_length=40,null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.username}"