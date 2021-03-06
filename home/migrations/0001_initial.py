# Generated by Django 3.2.13 on 2022-04-16 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=1000, verbose_name='Subtitle')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('background', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_item_background', to=settings.FILER_IMAGE_MODEL)),
            ],
        ),
    ]
