from core.models import SiteState
from django.db import transaction

def toggle_ssu():
    with transaction.atomic():
        state = SiteState.objects.select_for_update().get(pk=1)
        state.ssu_status = not state.ssu_status
        state.save(update_fields=["ssu_status", "updated_at"])
        return state.ssu_status
