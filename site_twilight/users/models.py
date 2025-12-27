from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    # Disable normal auth
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=128, blank=True)
    
    roblox_id = models.BigIntegerField(unique=True, null=True, blank=True)
    roblox_username = models.CharField(max_length=100, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "id"

    def __str__(self):
        return f'Usuario {self.roblox_username} #{self.roblox_id}'