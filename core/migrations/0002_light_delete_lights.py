# Generated by Django 4.2.11 on 2024-03-09 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(max_length=255)),
                ('is_online', models.BooleanField(default=True)),
                ('brightness', models.IntegerField(default=100)),
                ('color', models.CharField(default='#ffffff', max_length=7)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='core.room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Lights',
        ),
    ]