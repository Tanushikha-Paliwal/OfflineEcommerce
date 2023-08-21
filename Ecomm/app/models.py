from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email  = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

class Product(models.Model):
    Pname =  models.CharField(max_length=200)
    Description = models.TextField()
    image = models.ImageField(upload_to="product")