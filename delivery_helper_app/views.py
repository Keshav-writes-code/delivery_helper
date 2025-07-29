from django.shortcuts import render, redirect
from .models import user_types, Profile
from django.contrib.auth import login
from .forms import RegisterForm


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = RegisterForm()
    print(form.errors)
    context = {"user_types": user_types.objects.all(), "form": form}
            redirect(user.profile.user_type_id.type_name)
    return render(request, "registration/signup.html", context)
