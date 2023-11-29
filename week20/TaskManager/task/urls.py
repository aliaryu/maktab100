
from django.urls import path
from .views import task_detail

app_name = 'task'

urlpatterns = [
    path("task/<int:pk>", task_detail, name="task_detail"),
    path("task/delete/<int:pk>", task_detail, name="task_delete"),
    path("task/complete/<int:pk>", task_detail, name="task_complete"),

    path("category/<int:pk>", task_detail, name="category_detail"),
    path("tag/<int:pk>", task_detail, name="tag_detail"),


]
