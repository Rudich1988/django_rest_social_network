from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import F

from apps.likes.serializers import LikeSerializer
from apps.likes.models import Like
from apps.likes.permissions import IsOwner


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.select_related('user', 'post').all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    http_method_names = ('post', 'get', 'delete')

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (IsAuthenticated(),)
        return (IsOwner(),)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError(
                {'error': 'like already exists'}
            )

    def perform_destroy(self, instance):
        post = instance.post
        post.likes_count = F('likes_count') - 1
        post.save()
        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(
            queryset,
            many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
