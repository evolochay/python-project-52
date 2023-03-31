from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Status(models.Model):
    time_create = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name
