from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class KanbanLogin(auth_views.LoginView):
    template_name = 'registration/login.html'
    extra_context = {'next': reverse_lazy('index')}