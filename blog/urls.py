from django.urls import path

from . import views
from  .views import BlogList,createBlog,EditBlog,DeleteBlog,UserList,CommentView,CommentDetail

urlpatterns = [
     
    
    # path('add_blog/', views.submitBlog, name='add_blog'),
    path('create_blog/', createBlog.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>',EditBlog.as_view() , name='edit_blog'),
    path('delete_blog/<int:pk>',DeleteBlog.as_view() , name='delete_blog'),
    path('user_dashboard/<int:pk>',UserList.as_view(),name='user_dashboard'),
    path('like/<int:pk>',views.liked_blog, name='like'),
    path('/comments/<int:pk>',CommentView.as_view() , name='comments'),
    path('<int:pk>/commentView/', CommentDetail.as_view(), name='commentDetail'),
]