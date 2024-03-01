from django.db import models

from apps.Products.models import Product


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons', verbose_name="Продукт")
    name = models.CharField(max_length=255, verbose_name="Название урока")
    video_link = models.URLField(verbose_name="Ссылка на видео")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
