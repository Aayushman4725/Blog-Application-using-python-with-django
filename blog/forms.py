from blog.models import Blog
from django import forms

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