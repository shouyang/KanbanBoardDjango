from django.urls import reverse
from django.shortcuts import  get_object_or_404
from django.views.generic import RedirectView


from ..models import Task

class TaskAction(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        action = kwargs.get('action')
        task_pk = kwargs.get('pk')

        task = get_object_or_404(Task, pk=task_pk)

        if action == 'increase_priority':
            task.priority += 1

        elif action == 'decrease_priority':
            task.priority -= 1

        elif action == 'increase_status':
            task.increase_status()

        elif action == 'decrease_status':
            task.decrease_status()

        elif action == 'max_priority':
            task.max_priority()

        elif action == 'min_priority':
            task.min_priority()
        task.save()
        return reverse('index')