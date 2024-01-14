from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsMessageViewSet.as_view({'get':'list','post': 'create'}), name='contact-us')]