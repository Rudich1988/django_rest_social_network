from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from rest_soc_network import views

from apps.users.views import CustomUserViewSet
from apps.categories.views import CategoryViewSet
from apps.posts.views import PostViewSet


router = routers.SimpleRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'get_token/',
        views.CustomTokenObtainPairView.as_view(),
        name='get_token'
    ),
    path(
        'refresh_token/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]

urlpatterns += router.urls
