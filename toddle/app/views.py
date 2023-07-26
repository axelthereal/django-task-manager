from django.shortcuts import render, redirect
from django.http import HttpResponse 

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
      template_name = "pages/signup.html"
      context = {
            "viewname": "Create an account"
      }
      return render(req, template_name, context)


    
def home_view(req): 
      template_name = "pages/home.html"
      context = {
            "viewname": "Home"
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

    
def logout(req): 
      return redirect("/signin")
