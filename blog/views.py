from django.shortcuts import render,redirect
from blog.models import Blog
from django.contrib.auth.models import User

# Create your views here.



def submitBlog(request):
    blog_title=request.POST['postTitle']
    blog=request.POST['postContent']
    Blog.objects.create(title=blog_title, blog=blog)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm-password']

        myUser = User.objects.create_user(username,email,password)

        myUser.save()
        return redirect('sign_in')
    
    return render(request, 'signup.html')


def blog(request):
    blog = Blog.objects.all()

    context ={
        'blog' : blog
    }
    return render(request, 'index.html', context)

def sign_in(request):
    return redirect('blog')