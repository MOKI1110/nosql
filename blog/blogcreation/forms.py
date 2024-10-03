from django import forms
from .models import BlogPost  # Adjust according to your model

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # Ensure that the model is defined correctly
        fields = ['title', 'content', 'image', 'video']  # Adjust fields as needed
