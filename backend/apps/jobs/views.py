#jobs/views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
import requests
from .serializers import JobSerializer

class JobViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny] 

    def list(self, request):
        query = request.query_params.get('q', '')
        params = {
            'app_id': '8b4326c4',
            'app_key': 'c5ac254dbcd7ffd334a80c341683b63e',
            'results_per_page': '10',
            'what': query,
        }
        try:
            response = requests.get('https://api.adzuna.com/v1/api/jobs/gb/search/1', params=params)
            response.raise_for_status()
            jobs = response.json()['results']
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=500)