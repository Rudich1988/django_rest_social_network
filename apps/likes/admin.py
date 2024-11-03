from django.contrib import admin

from apps.likes.models import Like
from apps.users.models import CustomUser
from apps.posts.models import Post


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    fields = ['post']
    readonly_fields = ['user']
    list_display = ['id', 'user', 'post']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
