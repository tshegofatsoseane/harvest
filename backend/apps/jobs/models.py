#jobs/models.py

from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    JOB_STATUS_CHOICES = [
        ('saved', 'Saved'),
        ('in_progress', 'In Progress'),
        ('applied', 'Applied'),
        ('awaiting_review', 'Awaiting Review'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES, default='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
