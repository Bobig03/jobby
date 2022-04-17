from django.contrib import admin

from . import models

@admin.register(models.CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_filter = ("title", "order", "is_active", "created_at", "updated_at")
    list_display = ("title", "order", "is_active", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("title", "subtitle")
    date_hierarchy = "created_at"


@admin.register(models.AccentItem)
class AccentItemAdmin(admin.ModelAdmin):
    list_filter = ("title", "order", "image_side", "is_active", "created_at", "updated_at")
    list_display = ("title", "order", "image_side", "is_active", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("title", "subtitle")
    date_hierarchy = "created_at"
