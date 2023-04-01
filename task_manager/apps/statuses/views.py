from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utilities.text import Message, TitleName
from django.urls import reverse_lazy


own_messages = Message()
titles = TitleName()


class StatuseListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses_list.html"
    context_object_name = "statuses"

    login_url = "login"

    def handle_no_permission(self):
        messages.warning(self.request, own_messages.login)
        return redirect(self.login_url)


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ["name"]
    login_url = "login"
    template_name = "create.html"
    success_url = reverse_lazy("statuses_list")
    success_message = own_messages.status_create
    extra_context = {"header": titles.create_status, "button_name": titles.create}

    def handle_no_permission(self):
        messages.warning(self.request, own_messages.login)
        return redirect(self.login_url)


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    login_url = 'login'
    template_name = 'create.html'
    success_url = reverse_lazy('statuses_list')
    success_message = own_messages.status_update
    extra_context = {'header': titles.update_status,
                     'button_name': titles.update}

    def handle_no_permission(self):
        messages.warning(self.request, own_messages.login)
        return redirect(self.login_url)
