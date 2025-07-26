from django.contrib.auth.models import AbstractUser, User
from django.db import models

class AppUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

