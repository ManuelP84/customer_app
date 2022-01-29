"""Products admin class"""

from django.contrib import admin

# Models
from products.models import Product, Tag


admin.site.register(Product)
admin.site.register(Tag)


