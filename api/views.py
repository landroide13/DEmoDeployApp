from django.shortcuts import render
from rest_framework import viewsets

from api.models import Task
from api.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer