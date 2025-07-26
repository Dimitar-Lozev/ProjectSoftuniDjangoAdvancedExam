from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser,Profile


@admin.register(AppUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)
    readonly_fields = ('user',)

