# Generated by Django 3.2.7 on 2021-09-21 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210921_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='title',
            new_name='image',
        ),
    ]
