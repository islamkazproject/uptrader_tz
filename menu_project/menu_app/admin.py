from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent')
    list_filter = ('name',)
    ordering = ('name', 'id')
    search_fields = ('name', 'url', 'named_url')


admin.site.register(MenuItem, MenuItemAdmin)