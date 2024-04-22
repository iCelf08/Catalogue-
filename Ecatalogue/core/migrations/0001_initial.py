# Generated by Django 5.0.4 on 2024-04-21 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(choices=[('non_available', 'Non-available'), ('available', 'Available')], default='available', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogue_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
