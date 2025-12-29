def get_current_user_service(user):
    if user.is_authenticated:
        return {
            "roblox_username": user.roblox_username,
            "id": user.id,
            "is_authenticated": True,
        }

    return {
        "is_authenticated": False
    }
