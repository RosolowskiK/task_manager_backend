from rest_framework import viewsets

from .serializer import TaskRootSerializer
from .serializer import TaskChildSerializer
from .models import TaskRoot
from .models import TaskChild


class TaskRootViewSet(viewsets.ModelViewSet):
    queryset = TaskRoot.objects.all()
    serializer_class = TaskRootSerializer


class TaskChildViewSet(viewsets.ModelViewSet):
    queryset = TaskChild.objects.all()
    serializer_class = TaskChildSerializer
