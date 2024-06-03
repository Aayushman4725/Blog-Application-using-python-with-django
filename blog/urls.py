from django.urls import path

from . import views


urlpatterns = [
     
     path('blog/',views.blog,name='blog'),
    path('add_blog/', views.submitBlog, name='add_blog'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/',views.signup, name='sign_up'),
]