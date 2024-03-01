from django.db import models
from django.contrib.auth.models import User
from apps.Products.models import Product


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups', verbose_name="Продукт")
    name = models.CharField(max_length=255, verbose_name="Название группы")
    min_users = models.PositiveIntegerField(verbose_name="Минимальное количество учеников")
    max_users = models.PositiveIntegerField(verbose_name="Максимальное количество учеников")
    users = models.ManyToManyField(User, related_name='user_groups', blank=True, verbose_name="Ученики")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ['name']
