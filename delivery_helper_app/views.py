from django.shortcuts import render
from .models import user_types


# Create your views here.
def sign_up(request):
    context = {"user_types": user_types.objects.all()}
    return render(request, "registration/signup.html", context)
