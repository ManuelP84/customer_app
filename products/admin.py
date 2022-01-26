"""Products admin class"""

from django.contrib import admin

# Models
from products.models import Product


admin.site.register(Product)


