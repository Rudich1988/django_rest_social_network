from django.contrib import admin

from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'text',
        'likes_count',
        'category'
    ]
    list_display = ['id', 'name']
    readonly_fields = ['user']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
