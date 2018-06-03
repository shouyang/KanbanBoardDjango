from django.contrib import admin


from .models import Task, TaskComment
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    pass

