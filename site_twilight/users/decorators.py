from django.http import HttpResponseForbidden
from functools import wraps

def require_staff_permission(permission: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required")

            if not request.user.has_permission(permission):
                return HttpResponseForbidden("Insufficient permissions")

            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
