from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from kanban.models import Task


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'kanban/task_create_form.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)

        if self.request.user.is_authenticated:
            kwargs['initial'].update( {'author': self.request.user.username} )

        return kwargs



class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'kanban/task_edit_form.html'
    success_url = reverse_lazy('index')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
