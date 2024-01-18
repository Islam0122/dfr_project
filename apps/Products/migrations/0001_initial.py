# Generated by Django 4.2.6 on 2024-01-18 16:28

import apps.Products.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('img1', models.ImageField(blank=True, null=True, upload_to=apps.Products.models.product_image_path, verbose_name='Изображение 1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to=apps.Products.models.product_image_path, verbose_name='Изображение 2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to=apps.Products.models.product_image_path, verbose_name='Изображение 3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to=apps.Products.models.product_image_path, verbose_name='Изображение 4')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('price', models.CharField(max_length=400, verbose_name='Цена')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='Рекомендовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Products.category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
