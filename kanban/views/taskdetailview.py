from django.views.generic import DetailView

from ..models import Task


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'kanban/task_detail.html'
