# Generated by Django 3.2.5 on 2021-08-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20210818_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allips',
            name='ips',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='allips',
            name='postname',
            field=models.TextField(blank=True, default=''),
        ),
    ]