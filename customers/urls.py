"""Customers URLs"""

# Django
from django.urls import path

# Views
from customers import views as customers_views


urlpatterns = [

    path('customers/', customers_views.customers, name='customers'),

]