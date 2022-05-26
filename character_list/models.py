from django.db import models

from users.models import User


class CharacterList(models.Model):

    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_owner')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")