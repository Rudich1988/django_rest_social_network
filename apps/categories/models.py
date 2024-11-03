from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True
    )

    class Meta:
        indexes = [
            models.Index(
                fields=['name'],
                name='category_name_idx'
            ),
        ]

    def __str__(self):
        return self.name
