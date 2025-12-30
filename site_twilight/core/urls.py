from django.urls import path, include
from . import views

urlpatterns = [
    path("auth/user/", views.api_get_current_user),
    path("ssu/", views.api_get_ssu_status),
    path("", include("characters.urls")),
]
