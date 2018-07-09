from . import Index

from ..models import Task


class UserTasks(Index):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        todo_tasks = Task.objects.filter(status='TODO', author=self.request.user.username)
        prog_tasks = Task.objects.filter(status='PROG', author=self.request.user.username)
        test_tasks = Task.objects.filter(status='TEST', author=self.request.user.username)
        done_tasks = Task.objects.filter(status='DONE', author=self.request.user.username)

        context['TODO_list'] = todo_tasks.order_by('-priority')[:15]
        context['PROG_list'] = prog_tasks.order_by('-priority')[:15]
        context['TEST_list'] = test_tasks.order_by('-priority')[:15]
        context['DONE_list'] = done_tasks.order_by('-priority')[:15]

        return context

