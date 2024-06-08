from django.shortcuts import render, redirect
from blog.models import Blog
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import BlogForm,BlogEdit

class BlogList(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['blogs'] = context['blogs'].filter(user=self.request.user)
        search_input = self.request.GET.get('search_area') or ''
        
        if search_input:
            context['blogs'] =  context['blogs'].filter(title__startswith=search_input)
        else:
            context['blogs'] = self.get_queryset()

        if self.request.user.is_authenticated:
            context['blogs'] = context['blogs'].filter(user=self.request.user)
        
        context['search_input'] = search_input
        return context
    
# class UserList(ListView):
#     model = Blog
#     template_name = 'blog_list.html'
#     context_object_name = 'blogs'  

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['blogs'] = context['blogs'].filter(user=self.request.user)
#         search_input = self.request.GET.get('search_area') or ''
        
#         if search_input:
#             context['blogs'] =  context['blogs'].filter(title__startswith=search_input)
#         else:
#             context['blogs'] = self.get_queryset()
        
#         context['search_input'] = search_input
#         return context



class createBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(createBlog, self).form_valid(form)

class EditBlog(LoginRequiredMixin ,UpdateView):
    model = Blog
    template_name = 'edit_blog.html'
    form_class = BlogEdit
    
    success_url = reverse_lazy('blog')

class DeleteBlog(LoginRequiredMixin ,DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    get_object_name = 'blog'
    success_url = reverse_lazy('blog')
    
