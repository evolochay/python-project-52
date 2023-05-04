from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from .models import Task
from .filter import TaskFilter
from task_manager.utilities.text import Message, TitleName

own_message = Message()
titles = TitleName()


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks_list.html"
    filterset_class = TaskFilter
    login_url = "login"

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "create.html"
    success_url = reverse_lazy("tasks_list")
    extra_context = {
        "header": titles.create_task, "button_name": titles.create
        }
    login_url = "login"

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, own_message.task_create)
        print("DEBUG: form_valid - success_url =", self.success_url)
        return super(TaskCreateView, self).form_valid(form)


class TaskShowView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "show_task.html"
    context_object_name = "task"
    login_url = "login"

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ["name", "description", "status", "executor", "labels"]
    template_name = "create.html"
    success_url = reverse_lazy("tasks_list")
    success_message = own_message.task_update
    extra_context = {
        "header": titles.update_task, "button_name": titles.update
        }
    login_url = "login"

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)


class TaskDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    login_url = "login"
    success_url = reverse_lazy("tasks_list")
    template_name = "delete.html"
    extra_context = {"del_title": titles.delete_status}
    success_message = own_message.task_delete

    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author.id

    def handle_no_permission(self):
        messages.error(self.request, own_message.login)
        return redirect("login")
