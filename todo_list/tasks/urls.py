from django.urls import path

from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

app_name = 'tasks'

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>', TaskRetrieveUpdateDestroyView.as_view())
]