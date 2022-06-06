from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    mobileno = models.BigIntegerField(unique=True)
    address = models.TextField(null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'username']
    USERNAME_FIELD = 'mobileno'
