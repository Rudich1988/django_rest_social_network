from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            if self.action == 'list':
                return (IsAuthenticated(),)
            return (IsAdminUser(),)
        else:
            return (IsAdminUser(),)
