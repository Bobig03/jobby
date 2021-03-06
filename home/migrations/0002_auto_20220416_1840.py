# Generated by Django 3.2.13 on 2022-04-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carouselitem',
            options={'ordering': ['order', 'created_at'], 'verbose_name': 'Carousel Item', 'verbose_name_plural': 'Carousel Items'},
        ),
        migrations.AddField(
            model_name='carouselitem',
            name='link',
            field=models.URLField(default='', max_length=1000, verbose_name='Link'),
            preserve_default=False,
        ),
    ]
