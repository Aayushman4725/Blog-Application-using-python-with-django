from django.urls import path

from . import views


urlpatterns = [
    path('add_blog/', views.submitBlog, name='add_blog'),
]