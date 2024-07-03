from django.shortcuts import render, redirect,get_object_or_404
from authenticate.models import Comment
from blog.models import Blog,Like
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import BlogForm,BlogEdit,ComentForm,EditProfileForm
from django.views import View
from django.contrib.auth.models import User
from authenticate.models import Profile
from django.contrib.auth import get_user_model



User=get_user_model()


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

        # if self.request.user.is_authenticated:
        #     context['blogs'] = context['blogs'].filter(user=self.request.user)
        
        context['search_input'] = search_input
        return context
    

class UserList(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'user_list.html'
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
            profile, created = Profile.objects.get_or_create(user=self.request.user)
            context['profile'] = profile
        
        context['search_input'] = search_input
        return context
    




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
    
    success_url = reverse_lazy('user_dashboard')
    def get_success_url(self):
        return reverse_lazy('user_dashboard', kwargs={'pk': self.request.user.pk})

class DeleteBlog(LoginRequiredMixin ,DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    get_object_name = 'blog'
    success_url = reverse_lazy('user_dashboard')
    
    def get_success_url(self):
        return reverse_lazy('user_dashboard', kwargs={'pk': self.request.user.pk})
    

def liked_blog(request, pk):
   
        blog = get_object_or_404(Blog, pk=pk)
        if not Like.objects.filter(user=request.user, blog=blog).exists():
            Like.objects.create(user=request.user, blog=blog)
        else:
            like = Like.objects.filter(user=request.user, blog=blog).first()
            like.delete()
        return render(request, 'like.html', {'b': blog})   # Make sure 'blog' is the correct name of the URL pattern for your blog list or detail view.

class CommentView(View):
    form_class = ComentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('blog')  # Replace with your actual success URL

    def get_blog(self, pk):
        # Fetch the Blog instance using pk
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None
    
    def post(self, request, pk, *args, **kwargs):
        blog = self.get_blog(pk)
        if blog is None:
            # Handle case where blog with given pk doesn't exist
            return render(request, '404.html')  # Example, customize as needed

        form = self.form_class(request.POST)
        if form.is_valid():
            # Assign the logged-in user to the 'user' field of the Comment instance
            form.instance.user = request.user
            # Assign the blog instance to the 'blog' field of the Comment instance
            form.instance.blog = blog
            form.save()  # Save the form instance to persist the comment
            return redirect(self.success_url)
        else:
            return render(request, 'comment.html', {'form': form, 'blog': blog})

class CommentDetail(ListView):
    model = Comment
    template_name = 'comentDetail.html'
    context_object_name = 'comments'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(blog_id=pk)


# def change_profile_pic(request,pk):
#     user = get_object_or_404(User, pk=pk)
    
class EditProfile(UpdateView):
    form_class = EditProfileForm
    template_name = 'EditProfile.html'
    
    success_url = reverse_lazy('user_dashboard')
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('user_dashboard', kwargs={'pk': self.request.user.pk})