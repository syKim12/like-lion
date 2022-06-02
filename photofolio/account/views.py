from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth

from photoapp.forms import SignupForm, LoginForm
from .models import Account
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
    if request.method == 'POST':
        """
        account = Account()
        account.username = request.POST['username']
        account.password = request.POST['password']
        """
        #user = User()
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도해보세요')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            #account = Account()
            new_user = User.objects.create_user(username=signup_form.cleaned_data['username'], password=signup_form.cleaned_data['password'])
            auth.login(request, new_user)
            """
            user = User()
            user.username = signup_form.cleaned_data['username']
            user.password = signup_form.cleaned_data['password']
            user.save()
            """
            return redirect('home')
    else:
        signup_form = SignupForm()
    return render(request, 'signup_form.html', {'form':signup_form})