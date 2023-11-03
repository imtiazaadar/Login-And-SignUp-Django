# Name: Imtiaz Adar
# Project: Login And Register Using Django
# Language: Python
# Phone: 01778767775
# Email: imtiazadarofficial@gmail.com

from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# homepage
def Home_page(request):
    return render(request, 'index.html')

# login method
def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, (f'Congratulation {user.first_name} {user.last_name}, Login Successful !'))
                    return redirect('index')
                else:
                    return HttpResponse('<h1>Account Is Not Active</h1>')
            else:
                return HttpResponse('<h1>Sorry! Try Again!</h1>')
            
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})

# signup method
def Signup(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, (f'Congratulation, Your Account Has Been Created Successfully !'))
            return redirect('login')
    else:
        user_form = SignUpForm()
    return render(request, 'signup.html', {'user_form': user_form})

# logout method
@login_required
def Logout(request):
    logout(request)
    messages.success(request, ('Logged Out Successfully !'))
    return redirect('login')