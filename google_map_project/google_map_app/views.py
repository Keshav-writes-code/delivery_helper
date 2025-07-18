from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import user_table
 
from django.http import HttpResponse
@login_required(login_url="/login")
def home(request):
    return render(request,"basic/home.html")
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = user_table.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username already exists try again')
            return redirect('/')
        user = user_table.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password=password)
        messages.info(request,'Account created successfully.')
        return redirect('/login/')
    return render(request, 'basic/register.html')
def login_req(request):
    if request.method == "POST":
    
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not user_table.objects.filter(username=username).exists():
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
def logout_page(request):
    logout(request)
    return redirect('/login/')
  