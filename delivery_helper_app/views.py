from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import user_types, User
from django.contrib.auth import login
from .forms import RegisterForm


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f"/{user.profile.user_type_id.type_name}/")

    else:
        form = RegisterForm()
    context = {"user_types": user_types.objects.all(), "form": form}
    return render(request, "registration/signup.html", context)


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url

        try:
            user = User.objects.get(id=self.request.user.id)
            return f"/{user.profile.user_type_id.type_name}/"
        except User.DoesNotExist:
            return "/login/"
