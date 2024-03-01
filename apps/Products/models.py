from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    start_date = models.DateTimeField(verbose_name="Дата и время старта")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.name

    def get_lesson_count(self):
        return self.lessons.count()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
