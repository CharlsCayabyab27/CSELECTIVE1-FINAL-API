# Generated by Django 5.0 on 2023-12-19 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cselect_app', '0002_product_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
    ]