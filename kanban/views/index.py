from django.views.generic import  TemplateView

from ..models import Task

class Index(TemplateView):
    template_name = 'kanban/index.html'


    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['TODO_list'] = Task.objects.filter(status='TODO').order_by('-priority')[:15]
        context['PROG_list'] = Task.objects.filter(status='PROG').order_by('-priority')[:15]
        context['TEST_list'] = Task.objects.filter(status='TEST').order_by('-priority')[:15]
        context['DONE_list'] = Task.objects.filter(status='DONE').order_by('-priority')[:15]

        return context

