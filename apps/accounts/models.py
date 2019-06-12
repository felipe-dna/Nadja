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


def get_post_file_picture(instance, filename):
    path = "users/{}/post/{}/image/{}".format(
        instance.owner.id, instance.id, filename)
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

    couple_name = models.CharField(max_length=200, blank=True, null=True)
    love_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    image = models.ImageField(upload_to=get_post_file_picture, max_length=500)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.owner_id})

    def __str__(self):
        return self.title
# + ------------------------------------------------------------------------- +
