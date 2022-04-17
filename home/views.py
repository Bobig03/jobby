from django.shortcuts import get_object_or_404, render

from .models import CarouselItem, AccentItem


def home(request):
    carousel_items = CarouselItem.objects.filter(is_active=True)
    accent_items = AccentItem.objects.filter(is_active=True)
    context = {"carousel_items": carousel_items, "accent_items": accent_items}

    return render(request, "home/index.html", context)
