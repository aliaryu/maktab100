
from django.urls import path
from .views import task_detail, task_delete, task_complete, category_detail, tag_detail, mine, categories, search

app_name = 'task'

urlpatterns = [
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("task/delete/<int:pk>/", task_delete, name="task_delete"),
    path("task/complete/<int:pk>/", task_complete, name="task_complete"),

    path("category/<int:pk>/", category_detail, name="category_detail"),
    path("tag/<int:pk>/", tag_detail, name="tag_detail"),

    path("mine/", mine, name="mine"),
    path("categories/", categories, name="categories"),

    path("search/", search, name="search")
]
