# Generated by Django 3.2.7 on 2021-10-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20211007_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='order_status',
            field=models.CharField(choices=[('process', 'In Process'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='process', max_length=150),
        ),
    ]
