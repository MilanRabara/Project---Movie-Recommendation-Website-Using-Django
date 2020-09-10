from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default="xyz@abc.com")
    password = models.CharField(max_length=8)

# Name,Genre,Director,Cast, related name( fk )
