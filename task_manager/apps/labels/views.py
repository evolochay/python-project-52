from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from .models import Label
from task_manager.utilities.text import Message, TitleName

own_message = Message()
title = TitleName()


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels_list.html'
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)
    

class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'create.html'
    success_url = reverse_lazy('labels_list')
    login_url = 'login'
    success_message = own_message.label_create
    extra_context = {'header': title.create_label,
                     'button_name': title.create}

    def handle_no_permission(self):
        messages.warning(self.request, own_message.label_create)
        return redirect(self.login_url)
    
class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    login_url = 'login'
    template_name = 'create.html'
    success_url = reverse_lazy('labels_list')
    success_message = own_message.label_update
    extra_context = {'header': title.update_label,
                     'button_name': title.update}

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    login_url = 'login'
    success_url = reverse_lazy('labels_list')
    template_name = 'delete.html'
    extra_context = {'deltitle': title.delete_label}

    def handle_no_permission(self):
        messages.warning(self.request, own_message.login)
        return redirect(self.login_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, own_message.label_delete)
        except ProtectedError:
            messages.warning(self.request, own_message.no_delete_label)
        finally:
            return redirect(success_url)
