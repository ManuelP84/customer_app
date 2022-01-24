from django.shortcuts import render


def customers(request):
    return render(request, 'customers/customer.html')
