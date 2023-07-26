from django.db import models

# Create your models here.
class TaskModel(models.Model):
      title = models.CharField(max_length=150, null=False, blank=False)
      description = models.TextField(max_length=500, null=True, blank=True)
      created_at = models.DateTimeField()

      def __str__(self):
            return self.title
