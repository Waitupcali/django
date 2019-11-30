from django import forms
from .models import Blog

class PostForm(forms.ModelForm):

    class Meta: 
        model = Blog
        fields = {'title', 'description', 'myimage'}

# PostForm의 instance라고 봐야 하는 거임?
