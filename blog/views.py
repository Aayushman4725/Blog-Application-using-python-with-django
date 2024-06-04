from django.shortcuts import render,redirect
from blog.models import Blog


# Create your views here.



def submitBlog(request):
    blog_title=request.POST['postTitle']
    blog=request.POST['postContent']
    Blog.objects.create(title=blog_title, blog=blog)
    return redirect('blog')




def blog(request):
    blog = Blog.objects.all()

    context ={
        'blog' : blog
    }
    return render(request, 'index.html', context)

