from django.http import JsonResponse
from ..decorators import require_staff_permission
from site_twilight.services.ssu import toggle_ssu

@require_staff_permission("change_ssu_status")
def api_change_ssu_status(request):
    value = request.POST.get("value") == "true"
    status = toggle_ssu()
    return JsonResponse({"ssu_status": status})


@require_staff_permission("access_moderation_dashboard")
def api_moderation_dashboard(request):
    return JsonResponse({
        "ok": True,
        "role": "moderator",
    })
