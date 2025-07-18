from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
        user_type = request.POST.get('user_type')
        partner_id = request.POST.get('partner_id')
        password = make_password(request.POST.get('password'))
        user = User.objects.filter(username = user_id)
        if user.exists():
            messages.info(request,'Username already exists try again')
            return redirect('/')
        user = user_table.objects.create(
            user_id=user_id,
            name = name,
            email_id = email_id,
            phone_number =phone_number,
            user_type = user_type,
            partner_id =partner_id,
            password=password)

        
        messages.info(request,'Account created successfully.')
        return redirect('/login/')
    return render(request, 'basic/register.html')
def login_req(request):
    if request.method == "POST":
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid username.')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,'Invalid password.')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
        

    return render(request, 'basic/login.html')
def logout_button(request):
    logout(request)
    return redirect('/login/')
  