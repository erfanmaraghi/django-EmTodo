from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def time_since(timestamp):
    now = timezone.now()
    if now > timestamp:
        diff = now - timestamp
        if diff.days == 0:
            if diff.seconds < 60:
                return 'just now'
            elif diff.seconds < 120:
                return '1 minute ago'
            elif diff.seconds < 3600:
                return f'{diff.seconds // 60} minutes ago'
            elif diff.seconds < 7200:
                return '1 hour ago'
            else:
                return f'{diff.seconds // 3600} hours ago'
        elif diff.days == 1:
            return 'yesterday'
        else:
            return f'{diff.days} days ago'
    else:
        diff = timestamp - now
        if diff.days == 0:
            if diff.seconds < 60:
                return 'just now'
            elif diff.seconds < 120:
                return 'in 1 minute'
            elif diff.seconds < 3600:
                return f'in {diff.seconds // 60} minutes'
            elif diff.seconds < 7200:
                return 'in 1 hour'
            else:
                return f'in {diff.seconds // 3600} hours'
        elif diff.days == 1:
            return 'tomorrow'
        else:
            return f'in {diff.days} days'


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def added_time(self):
        return time_since(self.created_at)

    def __str__(self):
        return self.title
