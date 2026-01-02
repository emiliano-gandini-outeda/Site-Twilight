from django.urls import path, include
from . import views
from .api import users

urlpatterns = [
    path("auth/user/", views.api_get_current_user),
    path("ssu/", views.api_get_ssu_status),
    path("", include("characters.urls")),
    path("users/<int:roblox_id>/", users.api_get_user_by_roblox_id, name="api_get_user_by_roblox_id"),
    path("users/<int:roblox_id>/characters/", users.api_get_user_characters, name="api_get_user_characters"),
    path("", include("characters.urls")),
]
