from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="user_deleted")
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} written by {self.author} on {self.date_posted}"
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    