from django.urls import path
from .views import AboutUsViewSet

urlpatterns = [
    path('', AboutUsViewSet.as_view({'get': 'list'}), name='aboutus'),
                 ]
