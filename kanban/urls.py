from django.urls import path

from . import views

task_crud_patterns = [
    path('task/<uuid:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/add', views.TaskCreate.as_view(), name='task-add'),
    path('task/edit/<uuid:pk>', views.TaskUpdate.as_view(), name='task-edit'),
    path('task/delete/<uuid:pk>', views.TaskDelete.as_view(), name='task-delete'),
]

task_action_patterns = [
    path('task/actions/increase_priority/<uuid:pk>', views.TaskAction.as_view(), {'action': 'increase_priority'},
         name='task-action-increase_priority'),
    path('task/actions/decrease_priority/<uuid:pk>', views.TaskAction.as_view(), {'action': 'decrease_priority'},
         name='task-action-decrease_priority'),
    path('task/actions/increase_status/<uuid:pk>', views.TaskAction.as_view(), {'action': 'increase_status'},
         name='task-action-increase_status'),
    path('task/actions/decrease_status/<uuid:pk>', views.TaskAction.as_view(), {'action': 'decrease_status'},
         name='task-action-decrease_status'),
    path('task/actions/max_priority/<uuid:pk>', views.TaskAction.as_view(), {'action': 'max_priority'},
         name='task-action-max_priority'),
    path('task/actions/min_priority/<uuid:pk>', views.TaskAction.as_view(), {'action': 'min_priority'},
         name='task-action-min_priority'),
]

task_comment_crud_patterns = [
    path('task_comment/add/', views.TaskCommentCreate.as_view(), name='taskcomment-add'),
    path('task_comment/add/<uuid:task_pk>', views.TaskCommentCreate.as_view(), name='taskcomment-add-specific'),
    path('task_comment/edit/<uuid:pk>', views.TaskCommentUpdate.as_view(), name='taskcomment-edit-specific'),
    path('task_comment/delete/<uuid:pk>', views.TaskCommentDelete.as_view(), name='taskcomment-delete'),
]


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]

urlpatterns += task_crud_patterns
urlpatterns += task_action_patterns
urlpatterns += task_comment_crud_patterns
