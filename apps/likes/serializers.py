from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import F
from rest_framework.serializers import PrimaryKeyRelatedField

from apps.likes.models import Like
from apps.posts.models import Post


class LikeSerializer(
    serializers.ModelSerializer
):
    user = serializers.CharField(
        source='user.username',
        read_only=True
    )
    post = PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        write_only=True
    )
    post_name = serializers.CharField(
        source='post.name',
        read_only=True
    )

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'post_name']

    def get_post(self, obj):
        return obj.post.name

    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data.get('post')

        try:
            post = Post.objects.get(id=post.id)
        except Post.DoesNotExist:
            raise ValidationError(
                {'error': 'Post does not exist'}
            )

        like = Like.objects.create(
            user=user,
            post=post
        )

        post.likes_count = F('likes_count') + 1
        post.save()

        return like
