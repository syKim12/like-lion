from pyexpat import model
from django import forms
from .models import Post, Comment

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']