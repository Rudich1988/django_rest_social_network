from rest_framework import serializers

from apps.users.models import CustomUser
from apps.posts.serializers import PostSerializer


class CustomUserSerializer(
    serializers.ModelSerializer
):
    password = serializers.CharField(
        write_only=True
    )
    posts = PostSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'posts'
        ]

        extra_kwargs = {
            'posts': {'required': False},
        }

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(
            validated_data['password']
        )
        user.save()
        return user
