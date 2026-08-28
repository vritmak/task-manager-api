# api/views.py
from rest_framework import viewsets, filters # Add filters here
from django_filters.rest_framework import DjangoFilterBackend # Add this
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    # Add these three lines to enable the features:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']          # Enables ?completed=true
    search_fields = ['title', 'description'] # Enables ?search=keyword
    ordering_fields = ['created_at', 'title'] # Enables ?ordering=-created_at

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)