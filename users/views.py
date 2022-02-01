"""Users Views"""

# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from customers.models import Customer
#from django.contrib.auth.forms import UserCreationForm

# Forms
from . forms import CreateUserForm, CustomerForm

# Decorators
from . decorators import authenticated_user, allowed_users

@authenticated_user
def registerPage(request):
    """Register a new user"""
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for: ' + username)

            group = Group.objects.get(name='customers')
            user.groups.add(group)

            Customer.objects.create(user=user)
            
            return redirect('users:login')

    else:
        form = CreateUserForm()

    context = {'form': form}

    return render(
        request=request,
        template_name='users/register.html',
        context=context
    )


@authenticated_user
def loginUser(request):
    """Login an user"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request=request, 
            username=username, 
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('accounts:accounts')
        else:
            messages.info(request, 'Password or Username invalid!')


    context = {}

    return render(
        request=request,
        template_name='users/login.html',
        context=context
    )


@login_required
def logoutUser(request):
    """Logout an user"""

    logout(request)
    return redirect('users:login')


@login_required
@allowed_users(allowed_roles=['customers'])
def profileSettingsView(request):
    """Profile settings view"""

    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context={'form': form}

    return render(
        request=request,
        template_name='users/profile_settings.html',
        context=context
    )



