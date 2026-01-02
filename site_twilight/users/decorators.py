from django.http import HttpResponseForbidden
from functools import wraps
from django.http import JsonResponse

def require_staff_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Debug logging
            print(f"Permission check for: {permission}")
            print(f"User: {request.user.username if request.user else 'Anonymous'}")
            print(f"Is authenticated: {request.user.is_authenticated if request.user else False}")
            
            if not request.user.is_authenticated:
                return JsonResponse({"error": "Authentication required"}, status=401)
            
            if request.user.has_permission(permission):
                return view_func(request, *args, **kwargs)
            
            # Debug: List all user permissions
            print(f"User permissions check failed for: {permission}")
            # You might want to add: print(f"User has permissions: {list_user_permissions(request.user)}")
            
            return JsonResponse({"error": "Insufficient permissions"}, status=403)
        return _wrapped_view
    return decorator