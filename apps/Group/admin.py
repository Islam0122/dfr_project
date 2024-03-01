from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'min_users', 'max_users')


admin.site.register(Group, GroupAdmin)
