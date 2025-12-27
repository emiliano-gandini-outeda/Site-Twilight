from django.urls import path
from . import views

urlpatterns = [
    path("login/roblox/", views.roblox_login, name="roblox_login"),
    path("login/roblox/callback/", views.roblox_callback, name="roblox_callback"),
    path("logout/", views.logout_view, name="logout"),
]
