from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']
        password1= request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')


            else:

             user=User.objects.create_user(username=username,password=password)
             user.save();
             return redirect('register')

        else:
            messages.info(request,"password not matching")
            return redirect('/')


    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        dob = request.POST['dob']
        Age = request.POST['Age']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        email = request.POST['email']
        user=User.objects.create_user(username=username,dob=dob,Age=Age,phone_number=phone_number,address=address,email=email)
        user.save()

        return redirect('/')
    else:
        messages.info(request,"your application has been accepted")

        return render(request,'form.html')





