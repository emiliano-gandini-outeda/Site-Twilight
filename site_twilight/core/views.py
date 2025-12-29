from django.http import JsonResponse
from .models import SiteState
from .api.auth.user import get_current_user_service

# Create your views here.

def api_get_ssu_status(request):
    return JsonResponse({
        "ssu_status": SiteState.get().ssu_status
    })

def api_get_current_user(request):
    data = get_current_user_service(request.user)
    return JsonResponse(data)