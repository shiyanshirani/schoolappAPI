from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=150)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    email = models.EmailField(max_length=150, blank=True)
    address = models.TextField(max_length=250, blank=True)
    is_teacher = models.BooleanField()

    def __str__(self):
        return f"{self.user}"
