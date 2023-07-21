from django.urls import path
from .views import (
    default_view,
    signin_view,
    signup_view,
    home_view
    )

urlpatterns = [
        path("", default_view, name="default-view"),
        path("signin", signin_view, name="signin-view"),
        path("signup", signup_view, name="signup-view"),
        
        path("home", home_view, name="home-view"),

]