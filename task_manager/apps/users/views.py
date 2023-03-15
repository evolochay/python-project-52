from django.shortcuts import render
from django.views.generic import ListView
from task_manager.apps.users.models import User


class UserList(ListView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all
        return render(request, 'users_list.html', context={'users': users})
