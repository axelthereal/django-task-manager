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