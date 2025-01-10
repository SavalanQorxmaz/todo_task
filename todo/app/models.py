from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone
from utils.constants import *


class CustomUser(AbstractUser):
    is_premium = models.BooleanField(default=False)
    


class ToDoList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    label = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s To Do List"

class Task(models.Model):
    todo_list = models.ForeignKey(
        ToDoList, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)

    is_completed = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Ox"
        verbose_name_plural = "Oxen"
        ordering = ["title", "-created_at"]

    def __str__(self):
        return f"Task \"{self.title}\""
    
    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now() + timedelta(days=3)
            
        return super().save(*args, **kwargs)
    
    def show_due_data(self):
        return self.due_date.strftime("%d %b, %H:%M")
    
    def check_if_pin_available(self, **kwargs):
        user = kwargs.get('user')
        is_premium = user.is_premium
        max_pinned_available = \
            PremiumToDoListConfig.MAX_TASK_PIN_COUNT \
            if is_premium \
            else StandardToDoListConfig.MAX_TASK_PIN_COUNT
        pinned_tasks_count = self.objects.filter(is_pinned=True).count()
        return True if pinned_tasks_count < max_pinned_available else False
