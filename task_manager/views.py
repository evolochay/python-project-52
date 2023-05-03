from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "title": _("Task manager"),
        "description": _("A simple and functional task manager"),
    }


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "auth.html"
    success_message = _("You're logged in")


class LogoutUser(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("You're logged out"))
        return super().dispatch(request, *args, **kwargs)
