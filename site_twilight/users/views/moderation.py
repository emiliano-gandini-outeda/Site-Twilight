""" from ..decorators import require_staff_permission
from characters.models import Character
from django.shortcuts import redirect
from ..models import Warn, Ban
from django.http import JsonResponse

@require_staff_permission("view_characters_basic")
def api_characters_for_moderation(request):
    characters = (
        Character.objects
        .select_related("user", "faction", "access_card")
        .all()
    )

    data = [
        {
            "user": c.user.roblox_username,
            "name": c.display_name,
            "morph": c.morph_id,
            "faction": c.faction.display_name,
            "card": c.access_card.code,
            "status": c.status,
        }
        for c in characters
    ]

    return JsonResponse(data, safe=False)


@require_staff_permission("create_warn")
def create_warn(request, user_id):
    if request.method == "POST":
        Warn.objects.create(
            target_user_id=user_id,
            created_by=request.user,
            reason=request.POST["reason"],
        )
        return redirect("staff_warns")

@require_staff_permission("register_ban")
def register_ban(request, user_id):
    if request.method == "POST":
        Ban.objects.create(
            target_user_id=user_id,
            created_by=request.user,
            reason=request.POST["reason"],
        )
        return redirect("staff_bans")
    
@require_staff_permission("full_discord_moderation")
def api_discord_moderation_panel(request):
    return JsonResponse({
        "ok": True,
        "panel": "discord",
    })

from django.http import JsonResponse
from django.utils import timezone

@require_staff_permission("access_moderation_dashboard")
def manage_warns(request):
    if request.method == "GET":
        warns = Warn.objects.select_related("target", "created_by")

        data = [{
            "id": w.id,
            "user": w.target.roblox_username,
            "reason": w.reason,
            "created_at": w.created_at.isoformat(),
            "appealed": w.appealed,
        } for w in warns]

        return JsonResponse(data, safe=False)

    if request.method == "POST":
        if not request.user.has_permission("manage_warns"):
            return JsonResponse({"error": "forbidden"}, status=403)

        warn_id = request.POST.get("warn_id")
        warn = Warn.objects.get(id=warn_id)

        warn.appealed = True
        warn.appealed_at = timezone.now()
        warn.appealed_by = request.user
        warn.save()

        return JsonResponse({"ok": True})
 """