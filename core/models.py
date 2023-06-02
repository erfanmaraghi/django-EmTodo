from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
