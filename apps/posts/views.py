from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.permissions import IsAdminOrOwner


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related(
        'category'
    ).all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (IsAuthenticated(),)
        return (IsAdminOrOwner(),)
