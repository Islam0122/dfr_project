from apps.Basemodel.models import BaseModel
from django.utils.translation import gettext as _
from django.db import models


class Category(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")
