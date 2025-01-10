from django.contrib import admin

# Register your models here.
from .models import CustomUser, Task, ToDoList


admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(ToDoList)