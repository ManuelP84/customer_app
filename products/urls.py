"""Products URLs"""

# Django
from django.urls import path

# Views
from products import views as products_views


urlpatterns = [

    path('products/', products_views.products, name='products'),
]