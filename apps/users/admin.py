from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'created_at'
    ]
    search_fields = ['username', 'email']
