# Generated by Django 3.2.7 on 2021-10-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_useraddressbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressbook',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]