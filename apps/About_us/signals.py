from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import AboutUs

@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if AboutUs.objects.count() == 0:
        AboutUs.objects.create(
            description='Your default description here',
            location='Your default location here',
            telegram='https://t.me/your_default_telegram',
            instagram='https://t.me/your_default_telegram',
            whatsapp='Your default WhatsApp number here',
            phone_number='Your default phone numbers here',
            email='dujsobaevislam01@gmail.com'
        )