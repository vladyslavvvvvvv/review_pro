# Generated by Django 5.1.6 on 2025-03-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_review_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'reviewes'},
        ),
    ]
