"""Accounts URLs"""

# Django
from django.urls import path

# Views
from accounts import views as accounts_views


urlpatterns = [

    path('', accounts_views.account, name='accounts'),

]