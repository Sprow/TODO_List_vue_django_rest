from django.conf.urls import url

from task.views import CreateTaskView, DeleteTaskView, UpdateTaskView, ListTasksView


urlpatterns = [
    url(r'^api/list$', ListTasksView.as_view(), name='list_of_tasks'),
    url(r'^task/create$', CreateTaskView.as_view(), name='create_task'),
    url(r'^task/delete/(?P<task_id>[\d]+)$', DeleteTaskView.as_view(), name='delete_task'),
    url(r'^task/update/(?P<task_id>[\d]+)$', UpdateTaskView.as_view(), name='update_task'),
]
