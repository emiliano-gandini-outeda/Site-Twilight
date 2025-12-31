from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL


class Character(models.Model):
    # === Datos base ===
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters")

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    birth_date = models.DateField()

    codename = models.CharField(max_length=64, unique=True)
    faction = models.CharField(max_length=64)

    # === Morph data (todos opcionales) ===
    morph = models.CharField(max_length=255, blank=True)
    hat = models.CharField(max_length=255, blank=True)

    nvg_color = models.CharField(max_length=32, blank=True)

    shirt = models.CharField(max_length=64, blank=True)
    pants = models.CharField(max_length=64, blank=True)

    skin_r = models.PositiveSmallIntegerField(null=True, blank=True)
    skin_g = models.PositiveSmallIntegerField(null=True, blank=True)
    skin_b = models.PositiveSmallIntegerField(null=True, blank=True)

    ntag = models.CharField(max_length=128, blank=True)
    cntag_r = models.PositiveSmallIntegerField(null=True, blank=True)
    cntag_g = models.PositiveSmallIntegerField(null=True, blank=True)
    cntag_b = models.PositiveSmallIntegerField(null=True, blank=True)

    rtag = models.TextField(blank=True)
    crtag_r = models.PositiveSmallIntegerField(null=True, blank=True)
    crtag_g = models.PositiveSmallIntegerField(null=True, blank=True)
    crtag_b = models.PositiveSmallIntegerField(null=True, blank=True)

    rhat = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        morph_fields = [
            self.morph, self.hat, self.nvg_color,
            self.shirt, self.pants,
            self.skin_r, self.skin_g, self.skin_b,
            self.ntag,
            self.rtag,
        ]
        if not any(morph_fields):
            raise ValidationError("Al menos un campo de morph debe estar definido.")

    # ============================
    # Roblox command builder
    # ============================
    def morph_command(self):
        cmds = []
        
        # Obtener el nombre de usuario del owner
        username = self.owner.roblox_username if hasattr(self.owner, 'roblox_username') else str(self.owner)
        
        # Construir comandos individuales
        if self.morph:
            cmd = f"permmorph {username} {self.morph}"
            if self.rhat:
                cmd += f" & rhat {username}"
            cmds.append(cmd)
        
        if self.hat:
            cmds.append(f"permhat {username} {self.hat}")
        
        if self.shirt:
            cmds.append(f"permshirt {username} {self.shirt}")
        
        if self.pants:
            cmds.append(f"permpants {username} {self.pants}")
        
        if self.nvg_color:
            cmds.append(f"permcolornvg {username} {self.nvg_color}")
        
        if self.ntag:
            cmds.append(f'permntag {username} {self.ntag}')
        
        if None not in (self.cntag_r, self.cntag_g, self.cntag_b):
            cmds.append(
                f"permcntag {username} "
                f"{self.cntag_r} {self.cntag_g} {self.cntag_b}"
            )
        
        if self.rtag:
            cmds.append(f"permrtag {username} {self.rtag}")
        
        if None not in (self.crtag_r, self.crtag_g, self.crtag_b):
            cmds.append(
                f"permcrtag {username} "
                f"{self.crtag_r} {self.crtag_g} {self.crtag_b}"
            )
        
        # Agregar "run " al inicio y unir comandos con " & "
        if cmds:
            return f"run {' & '.join(cmds)}"
        return ""

    def __str__(self):
        return f"{self.codename} ({self.owner})"
