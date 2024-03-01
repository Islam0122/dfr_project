from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'video_link')
    search_fields = ('name', 'product__name')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'product', 'video_link'),
        }),
    )


admin.site.register(Lesson, LessonAdmin)
