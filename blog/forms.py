from blog.models import Blog
from django import forms
from django.contrib.auth.models import User
from authenticate.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'blog' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a blog'}),
        }

class BlogEdit(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput','placeholder': 'Enter a title'}),
            'blog' : forms.Textarea(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder':'Write the blog here...'}),
           
        }  

from django import forms


class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'comment_text']  # Assuming 'user' is a ForeignKey in the Comment model

        widgets = {
            'comment_text' : forms.Textarea(attrs={'class': 'form-control', 'id': 'floatingInput','placeholder': 'Enter a comment'}),
           
        }  


    def save(self, commit=True):
        comment_instance = super().save(commit=False)

        # Assuming 'user' is a ForeignKey in the Comment model
        user = comment_instance.user

        # Assuming you want to update the 'comment' field in the User model
        user.comment = comment_instance.comment_text  # Use 'comment_text' from Comment model

        # Save the User model instance if commit is True
        if commit:
            user.save()

        comment_instance.save()  # Save the Comment instance

        return comment_instance

