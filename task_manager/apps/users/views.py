from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
# from task_manager.apps.users.models import User
from task_manager.apps.users.forms import UserRegisterForm
from task_manager.utilities.text import TitleName, Message


title_names = TitleName()
own_messages = Message()


class UserListView(ListView):
    model = get_user_model()
    template_name = "users_list.html"
    context_object_name = "users"
    extra_context = {'title': _('Users'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('login')
    success_message = own_messages.user_create
    extra_context = {'header': title_names.reg,
                     'button_name': title_names.reg}
    

class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin,
                     UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('login')
    extra_context = {'header': title_names.update_user,
                     'button_name': title_names.save}

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = own_messages.no_rigths_for_user
            url = reverse_lazy('users_list')
        else:

            url = self.success_url
        messages.warning(self.request, message)
        return redirect(url)


class DeleteUserView(LoginRequiredMixin,
                     UserPassesTestMixin, DeleteView):
    model = get_user_model()
    template_name = 'delete.html'
    success_url = reverse_lazy('users_list')
    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id
