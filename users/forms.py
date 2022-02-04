"""Users Forms"""

# Django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django import forms

# Models
from customers.models import Customer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    privacy_policy = forms.BooleanField(required=True)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        widgets = {'privacy_policy': forms.HiddenInput()}


class ResetPasswordForm(PasswordResetForm):
    """Reset password form"""

    email = forms.CharField(
        min_length=6,
        max_length=70,
        label=False,
        widget=forms.EmailInput(
            attrs={
                'autocomplete':'email',
                'placeholder':'Email',
                'class':'form-control'
            }
        )
    )


class SetNewPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        max_length=70,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'New Password',
                'class':'form-control'
                }
            ),
    )
    new_password2 = forms.CharField(
        max_length=70,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Confirm New Password',
                'class':'form-control'
                }
            ),
        
    )
        


