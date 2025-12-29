from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .permissions import STAFF_PERMISSIONS

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, roblox_id, password=None, **extra_fields):
        if not roblox_id:
            raise ValueError("El usuario debe tener roblox_id")

        user = self.model(
            roblox_id=roblox_id,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, roblox_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(roblox_id, password, **extra_fields)

class User(AbstractUser):
    
    # Disable normal auth
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=128, blank=True)
    
    roblox_id = models.BigIntegerField(unique=True, null=True, blank=True)
    roblox_username = models.CharField(max_length=100, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "roblox_id"

    objects = UserManager()

    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    # Not RP related, only Django Backend
    is_staff = models.BooleanField(default=False)      # Django admin
    is_superuser = models.BooleanField(default=False)  # Django super admin

    def has_permission(self, permission: str) -> bool:
        for role in self.staff_roles.all():
            perms_by_level = STAFF_PERMISSIONS.get(role.scope, {})
            for lvl in range(1, role.level + 1):
                if permission in perms_by_level.get(lvl, set()):
                    return True
        return False

    def __str__(self):
        return f'Usuario {self.roblox_username} #{self.roblox_id}'

class StaffRole(models.Model):
    class Scope(models.TextChoices):
        GLOBAL = "global", "Moderation Lead"
        INGAME = "ingame", "In-Game Moderation"
        DISCORD = "discord", "Discord Moderation"
        ROLEPLAY = "roleplay", "Roleplay Moderation"

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="staff_roles",
    )

    scope = models.CharField(
        max_length=20,
        choices=Scope.choices,
    )

    level = models.PositiveSmallIntegerField(
        help_text="Higher level = more permissions"
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "scope")

    def __str__(self):
        return f"{self.user} | {self.scope} L{self.level}"

class Warn(models.Model):
    target = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="warns"
    )

    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="issued_warns"
    )

    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # opcional
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Warn -> {self.target.roblox_username}"
