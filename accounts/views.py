"""Accounts views"""

# Django
from django.shortcuts import render


def account(request):
    return render(request, 'accounts/dashboard.html')


