from django.contrib import admin
from .models import TaskModel, ProfileModel

# Register your models here.
admin.site.register(TaskModel)
admin.site.register(ProfileModel)