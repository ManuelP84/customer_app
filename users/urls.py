"""Users URLs"""

# Django
from django.urls import path

# Views
from . import views as users_views


urlpatterns = [

    path(
        route='register/',
        view=users_views.registerPage,
        name='register'
    ),

    path(
        route='login/',
        view=users_views.loginUser,
        name='login'
    ),

    path(
        route='logout/',
        view=users_views.logoutUser,
        name='logout'
    ),    

    path(
        route='profile_settings/',
        view=users_views.profileSettingsView,
        name='profile_settings'
    ),    
]