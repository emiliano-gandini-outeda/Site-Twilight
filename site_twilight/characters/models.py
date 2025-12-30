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
    def morph_command(self, user_placeholder="[USER]"):
        cmds = []

        if self.morph:
            cmd = f"run permmorph {user_placeholder} {self.morph}"
            if self.rhat:
                cmd += f" & rhat {user_placeholder}"
            cmds.append(cmd)

        if self.hat:
            cmds.append(f"permhat {user_placeholder} {self.hat}")

        if self.shirt:
            cmds.append(f"permshirt {user_placeholder} {self.shirt}")

        if self.pants:
            cmds.append(f"permpants {user_placeholder} {self.pants}")

        if self.nvg_color:
            cmds.append(f"permcolornvg {user_placeholder} {self.nvg_color}")

        if self.ntag:
            cmds.append(f'permntag {user_placeholder} {self.ntag}')

        if None not in (self.cntag_r, self.cntag_g, self.cntag_b):
            cmds.append(
                f"permcntag {user_placeholder} "
                f"{self.cntag_r} {self.cntag_g} {self.cntag_b}"
            )

        if self.rtag:
            cmds.append(f"permrtag {user_placeholder} {self.rtag}")

        if None not in (self.crtag_r, self.crtag_g, self.crtag_b):
            cmds.append(
                f"permcrtag {user_placeholder} "
                f"{self.crtag_r} {self.crtag_g} {self.crtag_b}"
            )

        return " & ".join(cmds)

    def __str__(self):
        return f"{self.codename} ({self.owner})"
