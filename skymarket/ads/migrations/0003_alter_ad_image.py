# Generated by Django 3.2.6 on 2023-02-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
