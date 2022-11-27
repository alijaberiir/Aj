from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField





class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(region="IR",null=False, blank=False, unique=True)
