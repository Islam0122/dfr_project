from django.contrib import admin
from .models import SellerProfile


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'phone_number', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'user__username', 'user__email', 'email', 'phone_number', 'address')
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'logo', 'name', 'description', 'phone_number', 'address', 'email', 'whatsapp_number',
                       'instagram_url', 'telegram_url', 'website')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
