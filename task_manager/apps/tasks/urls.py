from django.urls import path
from task_manager.apps.tasks.views import TaskListView, TaskCreateView, TaskShowView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('/<int:pk>/', TaskShowView.as_view(), name='task_show'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]