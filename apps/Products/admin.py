from django.contrib import admin
from .models import Product, Category
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


class RecommendationFilter(admin.SimpleListFilter):
    title = _('Рекомендация')
    parameter_name = 'is_recommended'

    def lookups(self, request, model_admin):
        return (
            ('all', _('Все товары')),
            ('recommended', _('Рекомендованные товары')),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'recommended':
            return queryset.filter(is_recommended=True)
        elif value == 'all':
            return queryset.all()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_recommended', 'created_at', 'updated_at')
    search_fields = ('name', 'category__title')
    list_filter = ('category__title', 'created_at', RecommendationFilter,)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'description', 'price'),
        }),
        ('Изображения', {
            'fields': ('img1', 'img2', 'img3', 'img4'),
        }),
        ('Дополнительные настройки', {
            'fields': ('is_recommended',),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'is_recommended':
            kwargs['widget'] = admin.widgets.AdminRadioSelect(choices=[(True, 'Да'), (False, 'Нет')])
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.is_recommended:
            recommended_count = Product.objects.filter(is_recommended=True).exclude(pk=obj.pk).count()
            if recommended_count >= 100:
                self.message_user(request, "Cannot set more than 100 products as recommended.", level="error")
                obj.is_recommended = False
        super().save_model(request, obj, form, change)
