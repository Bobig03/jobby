# Generated by Django 4.0 on 2022-04-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_postings', '0007_remove_jobposting_category_jobposting_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposting',
            name='category',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='postings', to='job_postings.Category', verbose_name='Categories'),
        ),
    ]
