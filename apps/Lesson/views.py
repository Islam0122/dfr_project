from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        return Lesson.objects.filter(product_id=product_id)
