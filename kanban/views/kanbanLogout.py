from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class KanbanLogout(auth_views.LogoutView):
    next_page = reverse_lazy('index')
    template_name = 'registration/logout.html'
