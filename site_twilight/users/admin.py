from django.contrib import admin

from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("roblox_id", "roblox_username", "is_staff", "is_superuser")