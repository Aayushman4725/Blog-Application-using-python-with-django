from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm-password']

        if User.objects.filter(username=username):
            messages.error(request, ("Username already exists!!"))
            return redirect('sign_up')
        
        if User.objects.filter(email=email):
            messages.error(request, ("Email already exists!!"))
            return redirect('sign_up')
        
        if password!=confirm:
            messages.error(request, ("Password did not match!!"))
            return redirect('sign_up')

        myUser = User.objects.create_user(username,email,password)

        myUser.save()
        return render(request, 'login.html')
    
    return render(request, 'signup.html')

def sign_in(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']  
       
       user = authenticate(username=username,password=password)

       if user is not None:
           login(request,user)
           return redirect('blog')

       else:
            messages.success(request, ("There was an error login in. Try again"))
            return redirect('home')
       
    return render(request , 'login.html')     
   