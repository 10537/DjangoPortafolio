from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    state = models.CharField(max_length=10, default='todo')

    def __str__(self):
        return self.title
