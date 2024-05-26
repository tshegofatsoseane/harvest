from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet
from .views import SavedJobListView

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('', include(router.urls)),
     path('saved-jobs/', SavedJobListView.as_view(), name='saved-jobs-list'),
]
