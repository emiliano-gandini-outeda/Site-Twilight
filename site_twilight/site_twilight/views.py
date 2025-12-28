from django.shortcuts import render
from django.http import JsonResponse
from .models import SiteState

def landingPage(request):
    return render(request, "index.html")

def api_get_ssu_status(request):
    return JsonResponse({
        "ssu_status": SiteState.get().ssu_status
    })
