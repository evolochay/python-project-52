from django.urls import path
from task_manager.apps.statuses.views import StatuseListView, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    path('', StatuseListView.as_view(), name='statuses_list'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
