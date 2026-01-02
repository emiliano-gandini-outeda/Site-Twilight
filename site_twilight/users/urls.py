from django.urls import path
from django.views.generic import RedirectView
from .views import accounts, moderation, permissions

urlpatterns = [
    path("login/roblox/", accounts.roblox_login, name="roblox_login"),
    path("login/roblox/callback/", accounts.roblox_callback, name="roblox_callback"),
    path('login/roblox/callback', 
         RedirectView.as_view(url='/accounts/login/roblox/callback/', permanent=True)),
    path("logout/", accounts.logout_view, name="logout"),
    
    # Dashboard
    path('moderation/dashboard/', moderation.api_moderation_dashboard, name='moderation_dashboard'),
    
    # Warns
    path('moderation/warns/', moderation.api_list_warns, name='list_warns'),
    path('moderation/warns/create/', moderation.api_create_warn, name='create_warn'),
    path('moderation/warns/<int:warn_id>/update/', moderation.api_update_warn, name='update_warn'),
    path('moderation/warns/<int:warn_id>/remove/', moderation.api_remove_warn, name='remove_warn'),
    
    # Appeals
    path('moderation/warns/<int:warn_id>/appeal/', moderation.api_appeal_warn, name='appeal_warn'),
    path('moderation/warns/<int:warn_id>/respond-appeal/', moderation.api_respond_appeal, name='respond_appeal'),
    
    # Bans
    path('moderation/bans/', moderation.api_list_bans, name='list_bans'),
    path('moderation/bans/create/', moderation.api_create_ban, name='create_ban'),
    path('moderation/bans/<int:ban_id>/revoke/', moderation.api_revoke_ban, name='revoke_ban'),
    
    # User-specific
    path('moderation/user/<int:roblox_id>/', moderation.api_get_user_moderation_info, name='user_moderation_info'),
    
    # Search users
    path('moderation/users/search/<str:query>/', moderation.api_search_users, name='search_users'),

    # Apeals
    path('moderation/user/appeals/', moderation.api_get_user_appeals, name='user_appeals'),
    
    # Characters
    path('moderation/characters/', moderation.api_characters_for_moderation, name='characters_moderation'),
    
    # Permissions
    path('auth/permissions/', permissions.api_get_user_permissions, name='user_permissions'),
    path('auth/user/', permissions.api_get_current_user, name='current_user'),
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