import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Character
from .forms import CharacterForm

@login_required
@require_http_methods(["POST"])
def character_create(request):
    data = json.loads(request.body)

    character = Character.objects.create(
        owner=request.user,
        first_name=data["first_name"],
        last_name=data["last_name"],
        country=data["country"],
        birth_date=data["birth_date"],
        codename=data["codename"],
        faction=data["faction"],

        morph=data.get("morph"),
        hat=data.get("hat"),
        nvg_color=data.get("nvg_color"),
        shirt=data.get("shirt"),
        pants=data.get("pants"),
        skin=data.get("skin"),
        ntag=data.get("ntag"),
        cntag=data.get("cntag"),
        rtag=data.get("rtag"),
        crtag=data.get("crtag"),
        rhat=data.get("rhat", False),
    )

    return JsonResponse({
        "id": character.id,
        "morph_command": character.morph_command(),
    }, status=201)


@login_required
@require_http_methods(["GET"])
def character_detail(request, pk):
    character = get_object_or_404(
        Character,
        pk=pk,
        owner=request.user
    )

    return JsonResponse({
        "id": character.id,
        "name": character.first_name,
        "last_name": character.last_name,
        "country": character.country,
        "birth_date": character.birth_date,
        "codename": character.codename,
        "faction": character.faction,
        "morph_command": character.morph_command(),
        "created_at": character.created_at,
    })

@login_required
@require_http_methods(["GET"])
def character_list(request):
    chars = Character.objects.filter(owner=request.user)

    return JsonResponse({
        "results": [
            {
                "id": c.id,
                "codename": c.codename,
                "faction": c.faction,
            }
            for c in chars
        ]
    })

@login_required
@require_http_methods(["GET"])
def character_list_all(request):
    characters = Character.objects.select_related("owner").all()

    return JsonResponse({
        "results": [
            {
                "id": c.id,

                # Identidad
                "first_name": c.first_name,
                "last_name": c.last_name,
                "country": c.country,
                "birth_date": c.birth_date,
                "codename": c.codename,

                # Ownership
                "owner_id": c.owner_id,
                "owner_username": c.owner.username,

                # Facción
                "faction": c.faction,

                # Morph
                "morph": c.morph,
                "hat": c.hat,
                "nvg_color": c.nvg_color,
                "shirt": c.shirt,
                "pants": c.pants,
                "skin": c.skin,
                "ntag": c.ntag,
                "cntag": c.cntag,
                "rtag": c.rtag,
                "crtag": c.crtag,
                "rhat": c.rhat,

                # Output
                "morph_command": c.morph_command(),

                # Meta
                "created_at": c.created_at,
                "updated_at": c.updated_at,
            }
            for c in characters
        ]
    })
