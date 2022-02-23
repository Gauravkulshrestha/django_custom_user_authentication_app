from urllib import request
from django.shortcuts import redirect, render
from .forms import MyUserForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate

def register(request):
    form = MyUserForm()
    if request.method == "POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyUserForm()
    context = {'form':form}

    return render(request, 'register.html',context)

def index(request):

    return render(request, 'index.html')

def password_change(request):
    chg_pwd_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        chg_pwd_form = PasswordChangeForm(request.POST)
        if chg_pwd_form.is_valid():
            chg_pwd_form.save()
            update_session_auth_hash(request, chg_pwd_form.user)            
            return redirect('home')
    else:
        chg_pwd_form = PasswordChangeForm(request.user)
    context = {'form':chg_pwd_form}
    return render(request, 'change-password.html', context)

def set_new_password(request):
    chg_pwd_form = SetPasswordForm(request.user)
    if request.method == "POST":
        chg_pwd_form = SetPasswordForm(request.POST)
        if chg_pwd_form.is_valid():
            chg_pwd_form.save()
            update_session_auth_hash(request, chg_pwd_form.user)            
            return redirect('home')
    else:
        chg_pwd_form = SetPasswordForm(request.user)
    context = {'form':chg_pwd_form}
    return render(request, 'set-new-password.html', context)    

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_user')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')