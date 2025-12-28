from django.shortcuts import render
from django.http import JsonResponse
from .models import SiteState
from django.http import HttpResponse


def landingPage(request):
    return render(request, "index.html")

def api_get_ssu_status(request):
    return JsonResponse({
        "ssu_status": SiteState.get().ssu_status
    })


def check_login(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Logged in as {request.user.roblox_username}")
    return HttpResponse("Not logged in")

def get_current_user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "roblox_username": request.user.roblox_username,
            "id": request.user.id,
            "is_authenticated": True
        })
    return JsonResponse({"is_authenticated": False})

