from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.urls import reverse, reverse_lazy
from .models import Task, ToDoList

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        todo_list = get_object_or_404(ToDoList, user=user)
        tasks = Task.objects.filter(todo_list=todo_list).select_related('todo_list')  # Optimallaşdırma
        context["task_list"] = tasks
        return context
# def home_page(request):
#     user = request.user
#     todo_list = get_object_or_404(ToDoList, user=user)
#     tasks = Task.objects.filter(todo_list=todo_list).select_related('todo_list')
#     context = {"task_list": tasks}
#     return render(request, "home.html", context )

class TaskCreateView(View):

    def post(self, request):
        user = request.user
        todo_list = ToDoList.objects.get(user=user)
        task_title = request.POST.get("task_title")
        task = Task.objects.create(
        todo_list=todo_list, 
        title=task_title
    )
        return redirect(reverse("app:index"))
# def create_new_task(request):
#     user = request.user
#     todo_list = ToDoList.objects.get(user=user)
#     task_title = request.POST.get("task_title")

#     task = Task.objects.create(
#         todo_list=todo_list, 
#         title=task_title
#     )
#     return redirect(reverse("app:index"))

class ChangeTaskStatusView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect(reverse("app:index"))
    
# def toggle_task_status(request, pk):
#     task = Task.objects.get(pk=pk)
#     task.is_completed = not task.is_completed
#     task.save()
#     return redirect(reverse("app:index"))


class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect(reverse("app:index"))

# def delete_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect(reverse("app:index"))

class ChangePinStatusView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        user = request.user
        is_available_to_pin = Task.check_if_pin_available(Task, user=user)
        if task.is_pinned:
            task.is_pinned = False
        else:
            if is_available_to_pin:
                task.is_pinned = True
        task.save()  
        return redirect(reverse("app:index"))

# def change_pin_situation(request, pk):
#     ready = False
#     task = Task.objects.get(pk=pk)
#     user = request.user
#     is_available_to_pin = Task.check_if_pin_available(Task, user=user)
#     if task.is_pinned:
#         task.is_pinned = False
#         ready = True
#     else:
#         if is_available_to_pin:
#             task.is_pinned = True
#             ready = True
#     task.save()  
#     return redirect(reverse("app:index"))

class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        context = {"task": task}
        return render(request, "task_detail.html", context )