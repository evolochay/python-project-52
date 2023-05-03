from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.db.models import ProtectedError
from task_manager.apps.users.forms import UserRegisterForm
from task_manager.utilities.text import TitleName, Message


titles = TitleName()
own_messages = Message()


class UserListView(ListView):
    model = get_user_model()
    template_name = "users_list.html"
    context_object_name = "users"
    extra_context = {
        "title": _("Users"),
        "btn_update": _("Update"),
        "btn_delete": _("Delete"),
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "create.html"
    success_url = reverse_lazy("login")
    success_message = own_messages.user_create
    extra_context = {"header": titles.reg, "button_name": titles.to_reg}


class UpdateUserView(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView
):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = "create.html"
    success_url = reverse_lazy("users_list")
    extra_context = {
        "header": titles.update_user, "button_name": titles.change
        }

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, own_messages.user_update)
        return redirect(self.success_url)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = own_messages.no_rigths
            url = reverse_lazy("users_list")
        else:
            message = own_messages.login
            url = self.success_url
        messages.warning(self.request, message)
        return redirect(url)


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = get_user_model()
    template_name = "delete.html"
    success_url = reverse_lazy("users_list")
    extra_context = {"del_title": titles.delete_user}

    def test_func(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return self.request.user.id == obj.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, own_messages.cant_delete_user)
            return redirect("users_list")
        else:
            return redirect(
                "%s?next=%s" % (reverse_lazy("login"), self.request.path)
                )

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, own_messages.user_delete)
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             own_messages.cant_delete_user)
            return redirect(success_url)
