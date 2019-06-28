from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('text',)


class UpdateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('task_status',)
