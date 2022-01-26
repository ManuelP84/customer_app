"""Accounts models"""

from django.db import models

class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # Customer
    # Product
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 200, null = True, choices =STATUS)

    def __str__(self):
        return self.name