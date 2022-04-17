from django.contrib import admin

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_at", "updated_at")
    list_display = ("name", "email", "phone", "website", "created_at", "updated_at")
    list_per_page = 15
    search_fields = (
        "name",
        "email",
        "phone",
        "website",
        "address",
        "short_description",
        "description",
    )
    date_hierarchy = "created_at"

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("name", "created_at", "updated_at")
    list_display = ("name", "created_at", "updated_at")
    list_per_page = 15
    search_fields = ("name",)
    date_hierarchy = "created_at"

@admin.register(models.JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_filter = ("title", "company", "categories", "created_at", "updated_at")
    list_display = (
        "title",
        "company",
        "location",
        "salary",
        "created_at",
        "updated_at",
    )
    list_per_page = 15
    search_fields = ("title", "location", "salary", "description")
    date_hierarchy = "created_at"
