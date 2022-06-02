from dataclasses import fields
from pyexpat import model
from django import forms
import django
from .models import Post, Comment
from account.models import Account
from django.contrib.auth.models import User

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']