from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path(
        "",
        views.home_page,
        name="index",
    ),
    path(
        "create-new-task/",
        views.create_new_task,
        name="create_new_task"
    ),
    path(
        "change-task-status/<int:pk>/",
        views.toggle_task_status,
        name="toggle_task_status"
    ),
    path(
        "delete-task/<int:pk>/",
        views.delete_task,
        name="delete_task"
    ),
     path(
        "change_pin_situation/<int:pk>/",
        views.change_pin_situation,
        name="change_pin_situation"
    )
]