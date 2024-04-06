from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Nickname

# Create your models here.

# Many-to-one
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    
class FirstName(models.Model):
    name = models.CharField(max_length=50)
    nick = models.OneToOneField(Nickname, on_delete=models.CASCADE)