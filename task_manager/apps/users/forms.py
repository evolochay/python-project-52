from task_manager.apps.users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name',
                  'password1', 'password2')
