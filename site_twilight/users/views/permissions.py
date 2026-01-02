# users/views/permissions.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import User
from users.permissions import STAFF_PERMISSIONS
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from users.decorators import require_staff_permission
import json
from django.shortcuts import get_object_or_404

@login_required
def api_get_user_permissions(request):
    """Obtener todos los permisos del usuario actual"""
    user = request.user
    
    # Obtener todos los permisos del usuario
    all_permissions = set()
    
    for role in user.staff_roles.all():
        perms_by_level = STAFF_PERMISSIONS.get(role.scope, {})
        for lvl in range(1, role.level + 1):
            if lvl in perms_by_level:
                all_permissions.update(perms_by_level[lvl])
    
    # Agregar permisos de superuser
    if user.is_superuser:
        all_permissions.update([
            'full_moderation_control',
            'full_discord_moderation',
            'access_moderation_dashboard',
            'create_warn',
            'register_ban',
            'manage_warns',
            'view_characters_basic',
            'change_ssu_status'
        ])
    
    # Agregar permisos de staff
    if user.is_staff:
        all_permissions.update([
            'access_moderation_dashboard',
            'view_characters_basic'
        ])
    
    return JsonResponse({
        'permissions': list(all_permissions),
        'scopes': [
            {
                'scope': role.scope,
                'level': role.level,
                'assigned_at': role.assigned_at.isoformat()
            }
            for role in user.staff_roles.all()
        ]
    })

@login_required
def api_get_current_user(request):
    """Obtener información del usuario actual"""
    user = request.user
    
    return JsonResponse({
        'id': user.id,
        'roblox_username': user.roblox_username,
        'roblox_id': user.roblox_id,
        'is_staff': user.is_staff,
        'is_superuser': user.is_superuser,
        'is_authenticated': user.is_authenticated,
        'first_login': user.first_login.isoformat() if user.first_login else None,
        'last_login': user.last_login.isoformat() if user.last_login else None,
        'warning_count': user.warning_count,
        'is_banned': user.is_banned,
    })

@csrf_exempt
@require_http_methods(["POST"])
@require_staff_permission("full_moderation_control")
def api_update_user_permissions(request, user_id):
    """Actualizar permisos de un usuario (solo admin)"""
    try:
        user = get_object_or_404(User, id=user_id)
        data = json.loads(request.body)
        permissions = data.get('permissions', [])
        
        # Aquí implementarías la lógica para guardar permisos
        # Por ahora solo retornamos éxito
        return JsonResponse({
            "success": True,
            "message": f"Permissions updated for {user.roblox_username}",
            "permissions": permissions
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_staff_permission("full_moderation_control")
def api_get_user_permissions_admin(request, user_id):
    """Obtener permisos de un usuario (vista admin)"""
    try:
        user = get_object_or_404(User, id=user_id)
        
        # Obtener todos los permisos del usuario
        all_permissions = set()
        
        for role in user.staff_roles.all():
            perms_by_level = STAFF_PERMISSIONS.get(role.scope, {})
            for lvl in range(1, role.level + 1):
                if lvl in perms_by_level:
                    all_permissions.update(perms_by_level[lvl])
        
        return JsonResponse({
            "permissions": list(all_permissions),
            "user": {
                "id": user.id,
                "roblox_username": user.roblox_username,
                "roblox_id": user.roblox_id,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser
            }
        })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)