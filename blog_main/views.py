from django.shortcuts import get_object_or_404, render
from blog.models import Blog


def home(request):
    blog = Blog.objects.all()

    context ={
        'blog' : blog
    }
    return render(request, 'index.html', context)
