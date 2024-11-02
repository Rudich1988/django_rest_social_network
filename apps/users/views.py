from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import CustomUser
from apps.users.serializers import CustomUserSerializer
from apps.users.permissions import IsOwnerOrAdmin


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method in ['POST']:
            return (AllowAny(),)
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return (IsOwnerOrAdmin(),)
        elif self.request.method == 'GET':
            if self.action == 'list':
                return (AllowAny(),)
            elif self.action == 'retrieve':
                return (IsOwnerOrAdmin(),)
        return super().get_permissions()
