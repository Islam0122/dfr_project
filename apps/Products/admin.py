from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'start_date', 'cost')
    search_fields = ('name', 'creator__username')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'creator', 'start_date', 'cost'),
        }),
    )


admin.site.register(Product, ProductAdmin)
