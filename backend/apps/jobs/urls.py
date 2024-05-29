#jobs/urls.py
from django.urls import path
from .views import JobViewSet

urlpatterns = [
    path('jobs/', JobViewSet.as_view({'get': 'list'}), name='job-list'),
]