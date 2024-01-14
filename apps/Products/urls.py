from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('<int:pk>/', views.ProductViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    })),

    path('recommended/', views.RecommendedProductViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('recommended/<int:pk>/', views.RecommendedProductViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('category/', views.CategoryViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    ]