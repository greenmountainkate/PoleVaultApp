from django import forms
from .models import Athlete

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)