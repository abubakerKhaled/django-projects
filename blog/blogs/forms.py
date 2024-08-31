from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'What is the title of the blog?', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={"cols": 80})}