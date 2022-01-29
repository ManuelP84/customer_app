"""Customers URLs"""

# Django
from django.urls import path

# Views
from . import views as customers_views


urlpatterns = [

    path(
        route='customer/<str:pk>/', 
        view=customers_views.customer, 
        name='customer'
    ),

    path(
        route='customers/list',
        view=customers_views.customersList,
        name='list'
    ),
]