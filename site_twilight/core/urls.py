from django.urls import path
from . import views

urlpatterns = [
    path("auth/user/", views.api_get_current_user),
    path("ssu/", views.api_get_ssu_status),
]
