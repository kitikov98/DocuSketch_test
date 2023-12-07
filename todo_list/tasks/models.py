from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
