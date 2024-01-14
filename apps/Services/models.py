from django.db import models
from apps.Basemodel.models import BaseModel
from django.utils.translation import gettext as _


class Service(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='service_photos/', height_field=None, width_field=None, max_length=100)
    price = models.CharField(max_length=200, blank=True, null=True)
    is_recommended = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
