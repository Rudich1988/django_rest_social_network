# Generated by Django 5.1.2 on 2024-11-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_likes_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
