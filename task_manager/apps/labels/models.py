from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")

    def __str__(self):
        return self.name
