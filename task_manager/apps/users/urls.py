from django.urls import path
from task_manager.apps.users import views


urlpatterns = [
    path("", views.UserListView.as_view(), name="users_list"),
    path("create/", views.UserCreateView.as_view(), name="user_create"),
    path("<int:pk>/update/", views.UpdateUserView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteUserView.as_view(), name="delete"),
]
