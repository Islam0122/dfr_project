from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from apps.Basemodel.models import BaseModel


class Category(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)

    def __str__(self):
        return self.title


def product_image_path(instance, filename):
    return f'Product_images/{slugify(instance.name)}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'


class Product(BaseModel):
    name = models.CharField(_('Название товара'), max_length=100)
    img1 = models.ImageField(_('Изображение 1'), upload_to=product_image_path, blank=True, null=True)
    img2 = models.ImageField(_('Изображение 2'), upload_to=product_image_path, blank=True, null=True)
    img3 = models.ImageField(_('Изображение 3'), upload_to=product_image_path, blank=True, null=True)
    img4 = models.ImageField(_('Изображение 4'), upload_to=product_image_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(_('Описание товара'), blank=True, null=True)
    price = models.CharField(_('Цена'),max_length=400)
    is_recommended = models.BooleanField(_('Рекомендовано'), default=False)

    class Meta:
        verbose_name = _("товар")
        verbose_name_plural = _("товары")

    def __str__(self):
        return self.name
