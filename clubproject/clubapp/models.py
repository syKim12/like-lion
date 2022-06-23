from re import T
from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.TextField(max_length=100)
    num_clubmember = models.IntegerField()
    photo = models.ImageField(blank=True, null=True, upload_to='photo')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
