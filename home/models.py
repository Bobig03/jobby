from django.db import models
from django.utils.translation import gettext_lazy as _

from filer.fields.image import FilerImageField

LEFT = "left"
RIGHT = "right"

IMAGE_SIDE_CHOICES = ((LEFT, _("Left")), (RIGHT, _("Right")))

class CarouselItem(models.Model):
    title = models.CharField(_("Title"), max_length=1000)
    subtitle = models.CharField(_("Subtitle"), max_length=1000)
    link = models.URLField(_("Link"), max_length=1000)
    background = FilerImageField(
        related_name="carousel_items", on_delete=models.CASCADE
    )
    order = models.IntegerField(_("Order"))
    is_active = models.BooleanField(_("Is active"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)


    class Meta:
        verbose_name = _("Carousel Item")
        verbose_name_plural = _("Carousel Items")
        ordering = ["order", "created_at"]


    def __str__(self):
        return self.title

class AccentItem(models.Model):
    title = models.CharField(_("Title"), max_length=1000)
    subtitle = models.CharField(_("Subtitle"), max_length=1000)
    link = models.URLField(_("Link"), max_length=1000)
    image = FilerImageField(
        related_name="accent_items", on_delete=models.CASCADE
    )
    image_side=models.CharField(_("Image side"), max_length=5, choices=IMAGE_SIDE_CHOICES, default=LEFT)
    order = models.IntegerField(_("Order"))
    is_active = models.BooleanField(_("Is active"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)


    class Meta:
        verbose_name = _("Accent Item")
        verbose_name_plural = _("Accent Items")
        ordering = ["order", "created_at"]


    def __str__(self):
        return self.title
