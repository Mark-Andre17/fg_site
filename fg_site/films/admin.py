from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    readonly_fields = ["get_image"]
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="50" height="60">')

    get_image.short_description = "Постер"


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image')
    readonly_fields = ["get_image"]
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="50" height="60">')

    get_image.short_description = "Постер"


class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'get_image', 'budget')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["get_image"]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="80" height="100">')

    get_image.short_description = "Постер"


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Actor, ActorAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Film, FilmAdmin)
