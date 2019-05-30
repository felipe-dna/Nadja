import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# + ------------------------------------------------------------------------- +
def get_profile_image_path(instance, filename):
    path = "users/{}/profile/image/{}".format(instance.id, filename)
    return path


def get_profile_cover_path(instance, filename):
    path = "users/{}/profile/cover/{}".format(instance.id, filename)
    return path
# + ------------------------------------------------------------------------- +


# Models


# + ------------------------------------------------------------------------- +
class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4)

    # profile fields
    profile_image = models.ImageField(
        upload_to=get_profile_image_path, blank=True, null=True)
    profile_cover = models.ImageField(
        upload_to=get_profile_cover_path, blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse("accounts:list", kwargs={})

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
# + ------------------------------------------------------------------------- +
