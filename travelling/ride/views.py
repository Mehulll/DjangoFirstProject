from django.shortcuts import render,redirect
from .models import customer

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"index.html")

def homes(request):
    return render(request,"index.html")

def news(request):
    return render(request,"news.html")

def contact(request):
    return render(request,"contact.html")

def destination(request):
    return render(request,"destinations.html")

def login(request):
    return render(request,"login.html")

def booking(request):
    return render(request,"booking.html")

def signup(request):
    return render(request,"signup.html")

def signup1(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        cpassword = request.POST.get('confirmpassword')
        if password==cpassword:
            dict={
                'firstname':firstname,
                'lastname':lastname,
                'email':email,
                'password':password,
                'username':username,
                }
            new_obj = customer.objects.create(**dict)
            new_obj.save()
            return render(request,'index.html',{'data':dict})
    else:
        error = "Invalid method"
        return render(request,"signup.html",{'error':error})

def login1(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
    for i in range :
        if (email== customer.objects.get('email')) and (password==customer.objects.get('password')):
            return render(request,"/") 
        else:
            error= "Incorrect method"
            return render(request,"login.html",{'error':error})



