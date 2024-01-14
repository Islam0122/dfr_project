from django.contrib import admin
from .models import Service
from django.utils.translation import gettext_lazy as _

class RecommendationFilter(admin.SimpleListFilter):
    title = _('Рекомендация')
    parameter_name = 'is_recommended'

    def lookups(self, request, model_admin):
        return (
            ('all', _('Все услуги')),
            ('recommended', _('Рекомендованные услуги')),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'recommended':
            return queryset.filter(is_recommended=True)
        elif value == 'all':
            return queryset.all()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'is_recommended', 'created_at', 'updated_at')
    list_filter = (RecommendationFilter,)
    search_fields = ('name',)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'is_recommended':
            kwargs['widget'] = admin.widgets.AdminRadioSelect(choices=[(True, 'Да'), (False, 'Нет')])
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.is_recommended:
            recommended_count = Service.objects.filter(is_recommended=True).count()
            if recommended_count >= 10:
                self.message_user(request, "Cannot set more than three services as recommended.", level="error")
                obj.is_recommended = False
        super().save_model(request, obj, form, change)
