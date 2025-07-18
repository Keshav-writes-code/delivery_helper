from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import user_table 
from django.contrib.auth.hashers import make_password



@login_required(login_url="/login")
def home(request):
    return render(request,"basic/home.html")

def register(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')  # Ensure this is passed as int
        partner_id = request.POST.get('partner_id')

        user = user_table.objects.create_user(
                user_id=user_id,
                name=name,
                email_id=email_id,
                phone_number=phone_number,
                user_type=int(user_type),
                partner_id=partner_id,
                password=password  
            )

        
        messages.info(request,'Account created successfully.')
        return redirect('/login/')
    return render(request, 'basic/register.html')
def login_req(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # Check if user exists
        if not user_table.objects.filter(user_id=user_id).exists():
            messages.error(request, "Invalid user ID.")
            return redirect('/login/')

        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, "Invalid password.")
            return redirect('/login/')

    return render(request, 'basic/login.html')
        

def logout_button(request):
    logout(request)
    return redirect('/login/')
  