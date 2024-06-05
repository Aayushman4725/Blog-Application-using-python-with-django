from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/',views.signup, name='sign_up'),
    path('sign_out/',views.signout, name='sign_out'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
]
   
