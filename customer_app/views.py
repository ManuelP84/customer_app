"""Customer_app views"""

# Django
from django.shortcuts import render


def privacy(request):

    context = {}

    return render(
        request=request,
        template_name='accounts/privacy_policy.html',
        context=context
    )


