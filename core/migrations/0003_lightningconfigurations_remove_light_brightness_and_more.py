# Generated by Django 4.2.11 on 2024-03-09 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_light_delete_lights'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightningConfigurations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=7)),
                ('brightness', models.IntegerField(default=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='light',
            name='brightness',
        ),
        migrations.RemoveField(
            model_name='light',
            name='color',
        ),
        migrations.AddField(
            model_name='light',
            name='configurations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lightningconfigurations'),
        ),
    ]
