"""Accounts admin class"""

from django.contrib import admin

# Models
from accounts.models import Order


admin.site.register(Order)


