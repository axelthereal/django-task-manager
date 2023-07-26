from django.urls import path
from .views import (
    default_view,
    signin_view,
    signup_view,
    home_view,
    tasks_view,
    completed_tasks_view,
    pending_tasks_view,
    add_view,
    logout
    )

urlpatterns = [
        path("", default_view, name="default-view"),
        path("signin", signin_view, name="signin-view"),
        path("signup", signup_view, name="signup-view"),
        path("logout", logout, name="logout-view"),

        path("tasks", tasks_view, name="tasks-view"),
        path("create", add_view, name="add-view"),
        path("completed", completed_tasks_view, name="completed-tasks-view"),
        path("pending", pending_tasks_view, name="pending-tasks-view"),
        
        path("home", home_view, name="home-view"),

]