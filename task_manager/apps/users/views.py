from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from task_manager.apps.users.models import User
from task_manager.apps.users.forms import UserCreationForm


class UserListView(ListView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users_list.html', context={'users': users})


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'user_create.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')
        return render(request, 'user_create.html', {'form': form})
