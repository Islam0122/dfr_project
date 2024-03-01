from django.urls import path
from .views import LessonViewSet

urlpatterns = [
    path('', LessonViewSet.as_view({
        'get': 'list', 'post': 'create'
    }), name='lesson-list'),
    path('<int:pk>/', LessonViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }), name='lesson-detail'),
]