from django.db import models
from django.contrib.auth import get_user_model
import uuid 
from datetime import datetime

User = get_user_model()

# Create your models here.
class ProfileModel(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      id_user = models.IntegerField()
      fullnames = models.CharField(max_length=100, default="", blank=False, null=False)
      bio = models.TextField(blank=True)
      profileimg = models.ImageField(upload_to='profile_images', default='user-img.jpg') 
      location = models.CharField(max_length=100, blank=True)
      
      def __str__(self):
            return self.user.username
      
class TaskModel(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4)
      author = models.CharField(max_length=150, blank=False, null=False)
      title = models.CharField(max_length=150, null=False, blank=False)
      description = models.TextField(max_length=500, null=True, blank=True)
      created_at = models.DateTimeField()

      def __str__(self):
            return self.title
