# Django Imports
from django.db import models

# Inside Projects Imports
from accounts.models import CustomUser as User
from shop.models import Product


class Order(models.Model):
    customer = models.ForeignKey(User, related_name="orders")
    discount = models.DecimalField()
    delivery = models.IntegerField()
    payment = models.OneToOneField("Payment", related_name="order")


class Payment(models.Model):
    created_at = models.DateField(auto_now_add=True)
    amount = models.DecimalField()
    code = models.IntegerField()


class Address(models.Model):
    customer = models.ForeignKey(User, related_name="user")
    city = models.CharField(max_length=50)
    route = models.TextField()


class Delivery(models.Model):
    order = models.OneToOneField(Order, related_name="delivery")
    address = models.ForeignKey(Address, related_name="deliveries")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items")
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.DecimalField()
    discount = models.DecimalField(max_digits=6, decimal_places=2)
