from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from home.models import msg

# Create your views here.
def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        user = authenticate(username=username,pswd=password)

        if user is not None:  
            login(request,user)
            return redirect('homepage')
        else:
            return render(request,'index.html')
    return render(request, 'index.html')

def homepage(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def sale(request):
    return render(request,'sale.html')

def settings(request):
    return render(request,'settings.html')

def contactus(request):
    if request.method =="POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('contact') and request.POST.get('sites') and request.POST.get('feedback'):
            saverecord =  msg()
            saverecord.name= request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.contact = request.POST.get('contact')
            saverecord.sites = request.POST.get('sites')
            saverecord.msg = request.POST.get('feedback')
            saverecord.save()    
            messages.success(request,"Thank you for valuable suggestion!")   
            return render(request,'contactus.html')
        
    else:
       return render(request,'contactus.html')     