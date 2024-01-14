from django.urls import path
from . import views


urlpatterns = [

    path('', views.ServiceViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('<int:pk>/', views.ServiceViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    })),

    path('recommended/', views.RecommendedServiceViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('recommended/<int:pk>/', views.RecommendedServiceViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    }))]