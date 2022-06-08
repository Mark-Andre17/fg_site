from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class StudioAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GameGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'get_image', 'raiting')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["get_image"]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="80" height="100">')

    get_image.short_description = "Постер"


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Studio, StudioAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(GameGenre, GameGenreAdmin)
admin.site.register(Game, GameAdmin)
