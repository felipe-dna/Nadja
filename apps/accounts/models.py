import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
