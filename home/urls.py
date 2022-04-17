from django.urls import path
from django.views import generic

from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
