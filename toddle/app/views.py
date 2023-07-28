from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
      ProfileModel,
      TaskModel
)


# Create your views here.
def default_view(req):
      return redirect("/signin")
    
def signin_view(req): 
      template_name = "pages/signin.html"
      context = {
            "viewname": "Sign in"
      }
      return render(req, template_name, context)

    
def signup_view(req): 
      if req.method == 'POST':
        fullnames = req.POST['fullnames']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        passconf = req.POST['passwordconf']
        if password == passconf:
            if User.objects.filter(email=email).exists():
               messages.info(req, 'User already exists, try another email')
            elif User.objects.filter(username=username).exists():
               messages.info(req, 'User already exists, try another username')
            else:
                user = User.objects.create_user(fullnames=fullnames, username=username, email=email, password=password) 
                user.save()
                
                # login_user
                user_login = auth.authenticate(username=username, password=password)
                auth.login(req, user_login)

                # create profile  
                user_model = User.objects.get(username=username)
                new_profile = ProfileModel.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/home')
        else:
           messages.info(req, 'Passwords Not Matching') 
        return redirect("/register") 

      template_name = "pages/signup.html"
      context = {
            "viewname": "Create an account"
      }
      return render(req, template_name, context)


def logout(req): 
      return redirect("/signin")
    
def home_view(req): 
      template_name = "pages/home.html"
      context = {
            "viewname": "Home"
      }
      return render(req, template_name, context)

def add_view(req): 
      template_name = "pages/add_task.html"
      context = {
            "viewname": "Create a new task"
      }
      return render(req, template_name, context)
    
def tasks_view(req): 
      template_name = "pages/tasks.html"
      context = {
            "viewname": "All Tasks"
      }
      return render(req, template_name, context)

    
def completed_tasks_view(req): 
      template_name = "pages/completed_tasks.html"
      context = {
            "viewname": "All Tasks"
      }
      return render(req, template_name, context)
    

def pending_tasks_view(req): 
      template_name = "pages/pending_tasks.html"
      context = {
            "viewname": "All Tasks"
      }
      return render(req, template_name, context)

