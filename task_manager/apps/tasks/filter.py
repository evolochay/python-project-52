from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django import forms
from django.utils.translation import gettext as _
from task_manager.apps.tasks.models import Task
from task_manager.apps.labels.models import Label


class TaskFilter(FilterSet):
    def task_filter(self, queryset, name, value):
        if value:
            author = getattr(self.request, "user", None)
            queryset = queryset.filter(author=author)
        return queryset

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
    )

    self_task = BooleanFilter(
        label=_("My tasks only"),
        widget=forms.widgets.CheckboxInput(
            attrs={"name": "self_task", "title_id": "id_self_task"}
        ),
        method="task_filter",
    )

    class Meta:
        model = Task
        fields = ["status", "executor"]
