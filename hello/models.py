from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class adUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
class CartItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/')