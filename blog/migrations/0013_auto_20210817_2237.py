# Generated by Django 3.2.5 on 2021-08-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_ips'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allips', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Ips',
        ),
    ]
