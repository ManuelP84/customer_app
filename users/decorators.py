
# Django
from django.shortcuts import redirect
from django.http import HttpResponse


def authenticated_user(view_func):
    def wrapper(request):       # Can also include the arguments: *args, **kwargs

        if request.user.is_authenticated:
            return redirect('accounts:accounts')
        else:
            return view_func(request)
    return wrapper


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            if request.user.groups.exists():
                groups = request.user.groups.all()
                for group in groups:
                    if group.name in allowed_roles:
                        return view_func(request, *args, **kwargs)
                    
            return HttpResponse('Sorry, you are not allowed here!')         
        return wrapper
    return decorator



def admin_only(view_func):
    def wrapper(request):

        if request.user.groups.exists():
            groups = request.user.groups.all()

            for group in groups:
                    if group.name == 'admin':
                        return view_func(request)
                    if group.name == 'customers':
                        return redirect('customers:customer_page')     
            
    return wrapper
