from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
 #return HttpResponse("Hello Ridhima") 
 return render(request,"authentication/index.html")

def signup(request):
 if request.method=="POST":
  username=request.POST.get('username')
  fname=request.POST.get('fname')
  lname=request.POST.get('lname')
  email=request.POST.get('email')
  pass1=request.POST.get('pass1')
  pass2=request.POST.get('pass2')

  if User.objects.filter(username=username):
    messages.error(request, "Username already exist! Please try some other username.")
    return redirect('home')
  
  if User.objects.filter(email=email).exists():
    messages.error(request, "Email Already Registered!!")
    return redirect('home')
  
         
  if len(username)>20:
     messages.error(request, "Username must be under 20 charcters!!")
     return redirect('home')
        
  if pass1 != pass2:
     messages.error(request, "Passwords didn't matched!!")
     return redirect('home')
        
  if not username.isalnum():
    messages.error(request, "Username must be Alpha-Numeric!!")
    return redirect('home')
         
  myuser=User.objects.create_user(username,email,pass1)
  myuser.firstname=fname
  myuser.lastname=lname

  myuser.save()
  messages.success(request,"Your Account has been Successfully created.")
  
  return redirect('signin')
 return render(request,"authentication/signup.html")


def signin(request):
 
 if request.method=="POST":
   username=request.POST.get('username')
   pass1=request.POST.get('pass1')
   user=authenticate(username=username,password=pass1)
   
   if user and user.is_superuser:
     login(request,user)
     return redirect('/admin')

   if user is not None:
    login(request,user)
    fname=user.first_name
    return render(request,"authentication/index.html",{'fname':fname})
   else:
    messages.error(request,"Bad Credentials")
    return redirect('home')
 return render(request,"authentication/signin.html")


def signout(request):
 logout(request)
 messages.success(request,"Logged Out Successfully")
 return redirect('home')