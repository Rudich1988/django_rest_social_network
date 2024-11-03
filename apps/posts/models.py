from django.db import models
from apps.users.models import CustomUser
from apps.categories.models import Category


class Post(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()
    likes_count = models.IntegerField(
        default=0
    )
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

    class Meta:
        indexes = [
            models.Index(
                fields=['category'],
                name='posts_category_idx'
            ),
            models.Index(
                fields=['user'],
                name='posts_user_idx'
            ),
        ]

    def __str__(self):
        return f'{self.id}: {self.name}'
