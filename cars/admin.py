from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):

    def thumbnail(self, objects):
        return format_html('<img src="{}" width="40">'.format(objects.car_photo.url))

    thumbnail.short_description = 'car photo'
    list_display = ('car_title', 'thumbnail', 'color', 'milage', 'passengers', 'is_featured')
    list_display_links = ('car_title', 'color')
    search_fields = ('car_title', 'color','milage')
    list_filter = ('model', 'city', 'body_style')


admin.site.register(Car, CarAdmin)
