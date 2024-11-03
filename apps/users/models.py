from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(
                fields=['email'],
                name='customuser_email_idx'
            ),
        ]

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'{self.username}'
