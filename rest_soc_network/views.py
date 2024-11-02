from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import status

from apps.users.models import CustomUser


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(
            self,
            request: Request,
            *args,
            **kwargs
    ) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(
                username=username
            )
            if user.check_password(password):
                return super().post(request, *args, **kwargs)
            else:
                return Response(
                    {'error': 'password is not correct'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except:
            return Response(
                {'error': 'user not found'},
                status=status.HTTP_404_NOT_FOUND
            )
