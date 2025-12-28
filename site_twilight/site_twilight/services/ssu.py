from ..models import SiteState

def toggle_ssu():
    state = SiteState.get()
    state.ssu_status = not state.ssu_status
    state.save(update_fields=["ssu_status", "updated_at"])
    return state.ssu_status
