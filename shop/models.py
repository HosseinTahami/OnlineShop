from django.db import models


class Product(models.Model):
    price = models.DecimalField()
    discount = models.DecimalField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField()
    category = models.ForeignKey("Category", related_name="products")


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField()
