
from django.urls import path
from .views import task_detail

app_name = 'task'

urlpatterns = [
    path("task/<int:pk>", task_detail, name="task_detail"),
]
