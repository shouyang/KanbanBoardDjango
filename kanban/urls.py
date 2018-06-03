from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('task/<uuid:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/add', views.TaskCreate.as_view(), name='task-add'),
    path('task/edit/<uuid:pk>', views.TaskUpdate.as_view(), name='task-edit'),
    path('task/delete/<uuid:pk>', views.TaskDelete.as_view(), name='task-delete'),
]
