from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

from apps.categories.serializers import CategorySerializer
from apps.posts.models import Post
from apps.categories.models import Category


class PostSerializer(serializers.ModelSerializer):
    category = PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    user = serializers.CharField(
        source='user.username',
        read_only=True
    )
    likes_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'text',
            'category',
            'user',
            'likes_count'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(
            instance
        )
        representation['category'] = CategorySerializer(
            instance.category
        ).data['name']
        return representation
