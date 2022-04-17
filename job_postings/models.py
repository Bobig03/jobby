from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


class Company(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    email = models.EmailField(_("E-mail"))
    phone = models.CharField(_("Phone number"), max_length=15)
    address = models.CharField(_("Address"), max_length=200)
    description = RichTextUploadingField(_("Description"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = RichTextUploadingField(_("Description"))

    company = models.ForeignKey(
        Company,
        related_name="postings",
        on_delete=models.CASCADE,
        verbose_name=_("Company"),
    )
    categories = models.ManyToManyField(
        Category,
        related_name="postings",
        verbose_name=_("Categories"),
        blank=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Job Posting")
        verbose_name_plural = _("Job Postings")

    def __str__(self):
        return self.title
