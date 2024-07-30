# Generated by Django 5.0.7 on 2024-07-30 14:41

import django.db.models.deletion
import image_generation.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=image_generation.models.image_upload_to)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='image_generation.batch')),
            ],
        ),
    ]
