from django.db import models
from django.db.models import UniqueConstraint

from apps.posts.models import Post
from apps.users.models import CustomUser


class Like(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name='likes',
        on_delete=models.PROTECT
    )
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('user', 'post'),
                name='ix_like_user_post'
            )
        ]
