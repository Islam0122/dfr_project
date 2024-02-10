from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.Basemodel.models import BaseModel

ABOUT_US_IMAGES_UPLOAD_PATH = 'about_us_images/'


class AboutUs(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    image = models.ImageField(upload_to=ABOUT_US_IMAGES_UPLOAD_PATH, verbose_name='Изображение', blank=True)
    text = models.TextField(verbose_name='Содержание', max_length=304, help_text='Maximum length: 304 characters')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')
