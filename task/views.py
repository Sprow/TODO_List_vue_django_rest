from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView, ListAPIView

from task.serializers import TaskSerializer, CreateTaskSerializer
from task.models import Task
from rest_framework.permissions import AllowAny


class CreateTaskView(CreateAPIView):
    """
    create new task
    """
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class DeleteTaskView(APIView):
    """
    delete task
    """
    serializer_class = TaskSerializer

    def delete(self, request, task_id):
        task = self.get_object(task_id)
        task.delete()
        return Response({'delete': 'success'})

    def get_object(self, obj_id):
        try:
            return Task.objects.get(pk=obj_id)
        except Task.DoesNotExist:
            raise Http404


class UpdateTaskView(APIView):
    """
    update task
    """
    serializer_class = TaskSerializer

    def put(self, request, task_id):
        task = self.get_object(task_id)
        if task.task_status:
            task.task_status = False
            task.save()
        else:
            task.task_status = True
            task.save()
        return Response({task_id: 'task_status : {}'.format(task.task_status)})

    def get_object(self, obj_id):
        try:
            return Task.objects.get(pk=obj_id)
        except Task.DoesNotExist:
            raise Http404


class ListTasksView(ListAPIView):
    """
    list of all tasks
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
