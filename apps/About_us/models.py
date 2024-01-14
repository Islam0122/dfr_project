from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


class AboutUs(models.Model):
    description = models.TextField(_("Description"))
    location = models.CharField(_("Location"), max_length=255)
    telegram = models.URLField(_("Telegram"), max_length=255, null=True, blank=True)
    instagram = models.URLField(_("Instagram"), max_length=255, null=True, blank=True)
    whatsapp = models.CharField(_("WhatsApp"), max_length=255, null=True, blank=True)
    phone_number = models.CharField(_("Phone Numbers"), max_length=20)
    email = models.EmailField(_("Email"), null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = _("About Us")
