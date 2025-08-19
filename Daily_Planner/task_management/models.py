from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    morning = models.TextField()
    afternoon = models.TextField()
    evening = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_name'
    )