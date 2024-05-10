from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, null=True, blank=True, default="Hey, there! I'm writing on PyPress")

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
