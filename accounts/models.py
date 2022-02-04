"""Accounts models"""

# Django
from django.db import models

# Utilities
from datetime import datetime

# Models
from customers.models import Customer
from products.models import Product


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer =  models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 200, null = True, choices =STATUS)
    note = models.CharField(max_length = 200, null = True)


    def __str__(self):
        return self.product.name + " by@ " + self.customer.first_name # Can also include the date_created self.date_created.strftime("%m/%d/%Y, %H:%M:%S"

