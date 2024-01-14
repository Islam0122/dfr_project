from django.db import models
from django.contrib.auth.models import User
from apps.Basemodel.models import BaseModel


class SellerProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    logo = models.ImageField(upload_to='seller_logos/', blank=True, null=True, verbose_name='Логотип')
    name = models.CharField(max_length=255, verbose_name=' ФИО или Название компании')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Email')
    whatsapp_number = models.CharField(max_length=20, verbose_name='Номер WhatsApp',blank=False,null=False)
    instagram_url = models.URLField(blank=False,null=False, verbose_name='Instagram URL', help_text='URL for Instagram.')
    telegram_url = models.URLField(blank=False,null=False, verbose_name='Telegram URL', help_text='URL for Telegram.')
    website = models.URLField(blank=True, null=True, verbose_name='Веб-сайт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль продавца'
        verbose_name_plural = 'Профили продавцов'
