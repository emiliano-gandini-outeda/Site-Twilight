# Create your models here.
from django.db import models

class SiteState(models.Model):
    ssu_status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1  # force singleton
        super().save(*args, **kwargs)