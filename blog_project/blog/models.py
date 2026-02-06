from django.db import models
from django.contrib.auth.models import User  # Import the default User model

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,  # Use the default User model
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
