from django.urls import path
from task_manager.apps.users import views


urlpatterns = [
    path('', views.UserList.as_view(), name='users_list'),
]