#jobs/views.py

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        job = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(Job.JOB_STATUS_CHOICES).keys():
            job.status = new_status
            job.save()
            return Response({'status': 'status updated'})
        else:
            return Response({'error': 'Invalid status'}, status=400)
