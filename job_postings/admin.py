from django.contrib import admin

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_at", "updated_at")
    list_display = ("name", "email", "phone", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("name", "email", "phone")

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_at", "updated_at")
    list_display = ("name", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("name",)


@admin.register(models.JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_filter = ("title", "company", "category", "created_at", "updated_at")
    list_display = ("title", "company", "category", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("title", "description")
