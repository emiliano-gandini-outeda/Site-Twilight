# app/characters/views.py
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone

from .models import Character
from .forms import CharacterForm

@login_required
@require_http_methods(["GET"])
def character_list_all(request):
    search_query = request.GET.get('search', '')
    
    characters = Character.objects.select_related("owner").all().order_by('codename')
    
    if search_query:
        characters = characters.filter(
            Q(codename__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(owner__roblox_username__icontains=search_query)
        )
    
    return JsonResponse({
        "results": [
            {
                "id": c.id,
                "first_name": c.first_name,
                "last_name": c.last_name,
                "country": c.country,
                "birth_date": c.birth_date.strftime("%Y-%m-%d") if c.birth_date else None,
                "age": self._calculate_age(c.birth_date) if c.birth_date else None,
                "codename": c.codename,
                "owner_id": c.owner_id,
                "owner_username": c.owner.roblox_username,
                "faction": c.faction,
                "morph": c.morph,
                "hat": c.hat,
                "nvg_color": c.nvg_color,
                "shirt": c.shirt,
                "pants": c.pants,
                "skin_r": c.skin_r,
                "skin_g": c.skin_g,
                "skin_b": c.skin_b,
                "ntag": c.ntag,
                "cntag_r": c.cntag_r,
                "cntag_g": c.cntag_g,
                "cntag_b": c.cntag_b,
                "rtag": c.rtag,
                "crtag_r": c.crtag_r,
                "crtag_g": c.crtag_g,
                "crtag_b": c.crtag_b,
                "rhat": c.rhat,
                "morph_command": c.morph_command(),
                "created_at": c.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for c in characters
        ]
    })

def _calculate_age(self, birth_date):
    today = timezone.now().date()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

@login_required
@require_http_methods(["GET"])
def character_list_user(request):
    search_query = request.GET.get('search', '')
    
    characters = Character.objects.filter(owner=request.user).order_by('codename')
    
    if search_query:
        characters = characters.filter(
            Q(codename__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    return JsonResponse({
        "results": [
            {
                "id": c.id,
                "first_name": c.first_name,
                "last_name": c.last_name,
                "country": c.country,
                "birth_date": c.birth_date.strftime("%Y-%m-%d") if c.birth_date else None,
                "age": self._calculate_age(c.birth_date) if c.birth_date else None,
                "codename": c.codename,
                "faction": c.faction,
                "morph": c.morph,
                "hat": c.hat,
                "nvg_color": c.nvg_color,
                "shirt": c.shirt,
                "pants": c.pants,
                "skin_r": c.skin_r,
                "skin_g": c.skin_g,
                "skin_b": c.skin_b,
                "ntag": c.ntag,
                "cntag_r": c.cntag_r,
                "cntag_g": c.cntag_g,
                "cntag_b": c.cntag_b,
                "rtag": c.rtag,
                "crtag_r": c.crtag_r,
                "crtag_g": c.crtag_g,
                "crtag_b": c.crtag_b,
                "rhat": c.rhat,
                "morph_command": c.morph_command(),
                "created_at": c.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for c in characters
        ]
    })

@login_required
@require_http_methods(["GET"])
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    
    # Verificar si el usuario es el owner o tiene permisos globales
    is_owner = character.owner == request.user
    can_view_all = request.user.has_permission("view_all_characters")
    
    if not (is_owner or can_view_all):
        return JsonResponse({"error": "No tienes permiso para ver este personaje"}, status=403)
    
    return JsonResponse({
        "id": character.id,
        "first_name": character.first_name,
        "last_name": character.last_name,
        "country": character.country,
        "birth_date": character.birth_date.strftime("%Y-%m-%d") if character.birth_date else None,
        "age": _calculate_age(character.birth_date) if character.birth_date else None,
        "codename": character.codename,
        "faction": character.faction,
        "owner_id": character.owner_id,
        "owner_username": character.owner.roblox_username,
        "is_owner": is_owner,
        
        # Morph data
        "morph": character.morph,
        "hat": character.hat,
        "nvg_color": character.nvg_color,
        "shirt": character.shirt,
        "pants": character.pants,
        "skin_r": character.skin_r,
        "skin_g": character.skin_g,
        "skin_b": character.skin_b,
        "ntag": character.ntag,
        "cntag_r": character.cntag_r,
        "cntag_g": character.cntag_g,
        "cntag_b": character.cntag_b,
        "rtag": character.rtag,
        "crtag_r": character.crtag_r,
        "crtag_g": character.crtag_g,
        "crtag_b": character.crtag_b,
        "rhat": character.rhat,
        
        "morph_command": character.morph_command(),
        "created_at": character.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    })

@login_required
@require_http_methods(["POST"])
def character_create(request):
    try:
        data = json.loads(request.body)
        
        # Validar que haya al menos un campo de morph
        morph_fields = [
            data.get("morph"),
            data.get("hat"),
            data.get("nvg_color"),
            data.get("shirt"),
            data.get("pants"),
            data.get("ntag"),
            data.get("rtag"),
        ]
        
        if not any(morph_fields):
            return JsonResponse({"error": "Al menos un campo de morph debe estar definido."}, status=400)
        
        # Verificar si el codename ya existe
        if Character.objects.filter(codename=data.get("codename")).exists():
            return JsonResponse({"error": "Este codename ya está en uso."}, status=400)
        
        character = Character.objects.create(
            owner=request.user,
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            country=data.get("country", ""),
            birth_date=data.get("birth_date"),
            codename=data.get("codename", ""),
            faction=data.get("faction", ""),
            
            # Morph data
            morph=data.get("morph", ""),
            hat=data.get("hat", ""),
            nvg_color=data.get("nvg_color", ""),
            shirt=data.get("shirt", ""),
            pants=data.get("pants", ""),
            skin_r=data.get("skin_r"),
            skin_g=data.get("skin_g"),
            skin_b=data.get("skin_b"),
            ntag=data.get("ntag", ""),
            cntag_r=data.get("cntag_r"),
            cntag_g=data.get("cntag_g"),
            cntag_b=data.get("cntag_b"),
            rtag=data.get("rtag", ""),
            crtag_r=data.get("crtag_r"),
            crtag_g=data.get("crtag_g"),
            crtag_b=data.get("crtag_b"),
            rhat=data.get("rhat", False),
        )
        
        return JsonResponse({
            "success": True,
            "id": character.id,
            "morph_command": character.morph_command(),
        }, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@login_required
@require_http_methods(["PUT"])
def character_update(request, pk):
    try:
        character = get_object_or_404(Character, pk=pk)
        
        # Solo el owner puede editar
        if character.owner != request.user:
            return JsonResponse({"error": "No tienes permiso para editar este personaje"}, status=403)
        
        data = json.loads(request.body)
        
        # Actualizar campos
        character.first_name = data.get("first_name", character.first_name)
        character.last_name = data.get("last_name", character.last_name)
        character.country = data.get("country", character.country)
        
        if data.get("birth_date"):
            character.birth_date = data.get("birth_date")
        
        character.codename = data.get("codename", character.codename)
        character.faction = data.get("faction", character.faction)
        
        # Morph data
        character.morph = data.get("morph", character.morph)
        character.hat = data.get("hat", character.hat)
        character.nvg_color = data.get("nvg_color", character.nvg_color)
        character.shirt = data.get("shirt", character.shirt)
        character.pants = data.get("pants", character.pants)
        character.skin_r = data.get("skin_r", character.skin_r)
        character.skin_g = data.get("skin_g", character.skin_g)
        character.skin_b = data.get("skin_b", character.skin_b)
        character.ntag = data.get("ntag", character.ntag)
        character.cntag_r = data.get("cntag_r", character.cntag_r)
        character.cntag_g = data.get("cntag_g", character.cntag_g)
        character.cntag_b = data.get("cntag_b", character.cntag_b)
        character.rtag = data.get("rtag", character.rtag)
        character.crtag_r = data.get("crtag_r", character.crtag_r)
        character.crtag_g = data.get("crtag_g", character.crtag_g)
        character.crtag_b = data.get("crtag_b", character.crtag_b)
        character.rhat = data.get("rhat", character.rhat)
        
        # Validar que haya al menos un campo de morph
        morph_fields = [
            character.morph,
            character.hat,
            character.nvg_color,
            character.shirt,
            character.pants,
            character.ntag,
            character.rtag,
        ]
        
        if not any(morph_fields):
            return JsonResponse({"error": "Al menos un campo de morph debe estar definido."}, status=400)
        
        character.save()
        
        return JsonResponse({
            "success": True,
            "id": character.id,
            "morph_command": character.morph_command(),
        })
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@login_required
@require_http_methods(["DELETE"])
def character_delete(request, pk):
    try:
        character = get_object_or_404(Character, pk=pk)
        
        # Solo el owner puede eliminar
        if character.owner != request.user:
            return JsonResponse({"error": "No tienes permiso para eliminar este personaje"}, status=403)
        
        character.delete()
        
        return JsonResponse({"success": True})
        
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)