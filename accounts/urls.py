"""Accounts URLs"""

# Django
from django.urls import path

# Views
from accounts import views as accounts_views


urlpatterns = [

    path(
    route='',
    view=accounts_views.account, 
    name='accounts'
    ),

    path(
    route='create_order/<str:pk>/', 
    view=accounts_views.createOrder, 
    name='create_order'
    ),

    path(
        route='update_order/<str:pk>/',
        view=accounts_views.updateOrder,
        name='update_order'
    ),

    path(
        route='delete_order/<str:pk>/',
        view=accounts_views.deleteOrder,
        name='delete_order'
    ),
]