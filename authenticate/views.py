from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm-password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('sign_up')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('sign_up')
        
        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('sign_up')

        myUser = User.objects.create_user(username, email, password)
        myUser.is_active = False
        myUser.save()

        # Welcome Email
        subject = "Welcome to Blog App!!"
        message = f"Hello, {myUser.username}!!\nWelcome to Blog App!!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myUser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        messages.success(request, "Your account has been successfully created! Please activate your account by clicking the link sent in your email.")

        # Account activation email
        current_site = get_current_site(request)
        email_subject = "Activate your account for Blog App"
        message2 = render_to_string('email_confirmation.html', {
            'name': myUser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myUser.pk)),
            'token': generate_token.make_token(myUser)
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myUser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('sign_in')  # Redirect to sign_in after signup
    
    return render(request, 'signup.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
       
        user = authenticate(username=username, password=password)

        if user is not None:
           
            if user.is_active==True:  # Check if the user account is active
                login(request, user)
                return redirect('blog')  # Redirect to 'blog' after successful login
            else:
                messages.error(request, "Your account is not activated yet. Please activate your account by clicking the link sent to your email.")
                return redirect('sign_in')
        else:
            messages.error(request, "Could not login.Please make sure that you have activated your account by clicking the link sent to your email or invalid username or password. Please try again.")
            return redirect('sign_in')
       
    return render(request, 'login.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myUser = User.objects.get(pk=uid)  # Corrected from User.object to User.objects
    
    except (ValueError, TypeError, OverflowError, User.DoesNotExist):
        myUser = None
    
    if myUser is not None and generate_token.check_token(myUser, token):
        myUser.is_active = True
        myUser.save()
        login(request, myUser)
        return redirect('home')  # Redirect to 'home' after successful activation
    
    else:
        return render(request, 'activation_failed.html')

def signout(request):
    logout(request)
    messages.success(request,("Successfully signed out"))
    return redirect('home')
