from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.get_full_name()

    def __repr__(self):
        return f'{self.username}'
