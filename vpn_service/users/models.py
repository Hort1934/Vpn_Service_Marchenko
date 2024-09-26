from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_transferred = models.BigIntegerField(default=0)  # In bytes
    page_transitions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
