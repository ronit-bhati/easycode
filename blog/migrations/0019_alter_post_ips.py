# Generated by Django 3.2.5 on 2021-08-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_ips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ips',
            field=models.TextField(blank=True, default=None),
        ),
    ]