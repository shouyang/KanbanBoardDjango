from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from kanban.models import Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'kanban/task_create_form.html'
    success_url = reverse_lazy('index')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'kanban/task_edit_form.html'
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
