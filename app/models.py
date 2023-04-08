from django.db import models

class CartItem(models.Model):
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField(max_length=100)
    productquantity=models.IntegerField()



# Create your models here.