from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductWithLessonCountViewSet.as_view({
        'get': 'list'
    })),
    path('<int:pk>/', views.ProductWithLessonCountViewSet.as_view({'get': 'retrieve'}))
    ]