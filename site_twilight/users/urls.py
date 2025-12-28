from django.urls import path
from . import views

urlpatterns = [
    path("login/roblox/", views.accounts.roblox_login, name="roblox_login"),
    path("login/roblox/callback/", views.accounts.roblox_callback, name="roblox_callback"),
    path("logout/", views.accounts.logout_view, name="logout"),

]
"""     
    path("api/staff/moderation/", views.api_moderation_dashboard),
    path("api/staff/discord/", views.api_discord_moderation_panel),

    path("api/staff/ssu/", views.api_change_ssu_status),

    path("api/rp/doc/<int:doc_id>/", views.api_edit_rp_files_basic),
    path("api/rp/doc/full/<int:doc_id>/", views.api_edit_rp_files_full),

    path("api/rp/factions/", views.api_faction_moderation_basic),
    path("api/rp/factions/full/", views.api_faction_moderation_full),

    path("api/rp/actors/", views.api_supervise_actors_basic),
    path("api/rp/actors/full/", views.api_supervise_actors_full), """