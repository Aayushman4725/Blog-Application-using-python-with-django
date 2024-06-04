from django.urls import path

from . import views


urlpatterns = [
     
     path('blog/',views.blog,name='blog'),
    path('add_blog/', views.submitBlog, name='add_blog'),
   
]