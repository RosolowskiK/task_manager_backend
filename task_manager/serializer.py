from rest_framework import serializers
from .models import TaskRoot
from .models import TaskChild


class TaskChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskChild
        fields = ('id', 'name', 'done', 'task_root')


class TaskRootSerializer(serializers.ModelSerializer):
    task_children = TaskChildSerializer(many=True, read_only=True)
    task_children_count = serializers.SerializerMethodField()
    task_children_done = serializers.SerializerMethodField()

    class Meta:
        model = TaskRoot
        fields = ['id', 'name', 'description', 'task_children', 'task_children_count', 'task_children_done']

    def get_task_children_count(self, task_root):
        return task_root.task_children.count()

    def get_task_children_done(self, task_root):
        return task_root.task_children.filter(done=True).count()



