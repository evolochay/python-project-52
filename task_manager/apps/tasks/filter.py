import django_filters


class TaskFilter(django_filters.FilterSet):
    def task(self):
        return "class"