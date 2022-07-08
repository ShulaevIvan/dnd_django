from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserTokens(models.Model):

    user = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=999, unique=True)

