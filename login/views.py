from django.shortcuts import render_to_response, redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import Puser
from django.contrib.auth import *
from login.forms import *
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


def login1(request):  # view for login page...
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def signUp(request):  # view to show the signup page...
    c = {}
    c.update(csrf(request))
    c['role'] = 'member'
    return render(request, 'signup.html', c)

def auth_view(request):
     username = request.POST.get('username','')
     password= request.POST.get('password','')
     user = auth.authenticate(username=username, password=password)
     #p_user = Puser.objects.get(user_id = username)
     #print(username+password)
     #print(p_user.user_id+p_user.password)
     if user is not None:
          auth.login(request, user)
          return HttpResponseRedirect('/login/loggedin')
          #return render(request,'display_data.html')
     else:
          return HttpResponseRedirect('/login/invalidlogin')
          #return render(request,'signup.html')

@login_required(login_url= '/login1/')
def loggedin(request):  # view for redirecting valid user to home page...
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')


def invalidlogin(request):  # view to redirect the invalid user to login page...
    c = {}
    c.update(csrf(request))
    c['q'] = "Invalid Username or Password"
    return render(request, 'login.html', c)


def store(request):  # view to store the new user data in to datbase...
    username = request.POST.get('username', '')
    name = request.POST.get('name', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    date = request.POST.get('date', '')
    c = {}
    c.update(csrf(request))
    form =UserCreationForm(request.POST)
    c['form']=form;
    c['role'] = 'member'
    print(form.is_valid())
    if form.is_valid():
          profile = Puser(user_id=username, user_name=name,email=email,phoneno=phone,bdate=date,password=password1)
          profile.save()
          form.save()
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = auth.authenticate(username=username, password=raw_password)
          login(request, user)
          return render(request, 'login.html')
    return render(request, 'signup.html', c)

@login_required(login_url= '/login/')
def profile(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    user=User.objects.get(id=id)
    p=Puser.objects.get(user_id=user.username)
    c['user']=p
    return render(request,'profile.html',c)
@login_required(login_url= '/login/')
def logout(request):  # view for log out the user...
    auth.logout(request)
    return render(request, 'login.html')
