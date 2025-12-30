from django.urls import path
from . import views

urlpatterns = [
    path("characters/", views.character_list_all, name="character_list_all"),
    path("characters/create/", views.character_create, name="character_create"),
    path("characters/<int:pk>/", views.character_detail, name="character_detail"),
]
