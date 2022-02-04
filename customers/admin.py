"""Customer admin class"""

from django.contrib import admin

# Models
from customers.models import Customer


admin.site.register(Customer)

