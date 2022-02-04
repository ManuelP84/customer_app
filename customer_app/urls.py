"""Customer app URLs"""

# Django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.forms import SetNewPasswordForm, ResetPasswordForm

from django.conf.urls.static import static
from django.conf import settings

# Views
from . import views


urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),

    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('', include(('customers.urls', 'customers'), namespace='customers')),

    path('', include(('products.urls', 'products'), namespace='products')),

    # Reset passwors URLs
    path(
        route='reset_password/',
        view=auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            form_class=ResetPasswordForm
        ),
        name='reset_password'
    ),
    
    path(
        route='reset_password_sent/',
        view=auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'),
        name='password_reset_done'
    ),

    path(
        route='reset/<uidb64>/<token>/',
        view=auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_form.html',
            form_class=SetNewPasswordForm
        ),
        name='password_reset_confirm'
    ),

    path(
        route='reset_password_complete/',
        view=auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_complete'
    ),

    # Privacy policy URL
    path(
        route='privacy/',
        view=views.privacy,
        name='privacy'
    ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
