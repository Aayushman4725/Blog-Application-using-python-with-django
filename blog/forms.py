from blog.models import Blog
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog']

        widget = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title'}),
            'blog' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a blog'}),
        }

class BlogEdit(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog']

        widget = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog' : forms.TextInput(attrs={'class': 'form-control'}),
           
        }  