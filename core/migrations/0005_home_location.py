# Generated by Django 4.2.11 on 2024-03-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_lightningconfigurations_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
