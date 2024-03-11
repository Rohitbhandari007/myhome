# Generated by Django 4.2.11 on 2024-03-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='home_layouts')),
                ('is_online', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor', models.IntegerField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='core.home')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
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
    ]
