from django.urls import path
from django.views import generic

from . import views

urlpatterns = [
    path("postings", views.job_posting_list, name="job_posting_list"),
    path("postings/<int:id>/", views.job_posting_detail, name="job_posting_detail"),
    path("companies", views.company_list, name="company_list"),
    path("companies/<int:id>/", views.company_detail, name="company_detail"),
    path("categories", views.category_list, name="category_list"),
    path("categories/<int:id>/", views.category_detail, name="category_detail"),
]
