from dataclasses import fields
from pyexpat import model
from django import forms
import django
from .models import Club, Comment


class ClubForm(forms.Form):
    class Meta:
        model = Club
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

