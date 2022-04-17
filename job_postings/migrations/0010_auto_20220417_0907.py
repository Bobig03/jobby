# Generated by Django 3.2.13 on 2022-04-17 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('job_postings', '0009_alter_jobposting_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(default='', max_length=1000, verbose_name='Web site'),
            preserve_default=False,
        ),
    ]
