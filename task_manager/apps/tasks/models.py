from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(null=True, verbose_name=_("Description"))
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("Author"))
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name=_("Status")
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="executor",
        verbose_name=_("Executor"),
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))

    def __str__(self):
        return self.name
