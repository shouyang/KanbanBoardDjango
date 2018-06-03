import datetime

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from kanban.models import TaskComment

class TaskCommentCreate(CreateView):
    model = TaskComment
    fields = '__all__'
    template_name = 'kanban/taskcomment_create_form.html'

    def get_initial(self):
        return {'task': self.kwargs.get('task_pk')}

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk':self.object.task.uuid})


class TaskCommentUpdate(UpdateView):
    model = TaskComment
    fields = '__all__'
    template_name = 'kanban/taskcomment_create_form.html'

    def get_success_url(self):
        return reverse_lazy('task-detail', kwargs={'pk':self.object.task.uuid})


class TaskCommentDelete(DeleteView):
    model = TaskComment
    success_url = reverse_lazy('index')
