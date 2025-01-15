from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    # path(
    #     "",
    #     views.home_page,
    #     name="index",
    # ),
    path(
        '', 
        views.HomePageView.as_view(), 
        name='index'
        ),
    # path(
    #     "create-new-task/",
    #     views.create_new_task,
    #     name="create_new_task"
    # ),
    path(
        'create-new-task', 
        views.TaskCreateView.as_view(), 
        name='create_new_task'
        ),
    # path(
    #     "change-task-status/<int:pk>/",
    #     views.toggle_task_status,
    #     name="toggle_task_status"
    # ),
    path(
        "change-task-status/<int:pk>/",
        views.ChangeTaskStatusView.as_view(),
        name="toggle_task_status"
    ),
    # path(
    #     "delete-task/<int:pk>/",
    #     views.delete_task,
    #     name="delete_task"
    # ),
     path(
        "delete-task/<int:pk>/",
        views.DeleteTaskView.as_view(),
        name="delete_task"
    ),
    #  path(
    #     "change_pin_situation/<int:pk>/",
    #     views.change_pin_situation,
    #     name="change_pin_situation"
    # ),
      path(
        "change_pin_situation/<int:pk>/",
        views.ChangePinStatusView.as_view(),
        name="change_pin_situation"
    ),
        path(
        "task/<int:pk>/",
        views.TaskDetailView.as_view(),
        name="task_detail"
    ),
]