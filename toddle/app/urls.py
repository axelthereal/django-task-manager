from django.urls import path
from .views import (
    signin_view,
    default_view
    )

urlpatterns = [
        path("", default_view, name="default-view"),
        path("signin", signin_view, name="signin-view")
]