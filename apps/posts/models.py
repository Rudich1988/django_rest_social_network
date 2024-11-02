from django.db import models
from apps.users.models import CustomUser
from apps.categories.models import Category


class Post(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
