# Generated by Django 3.0.4 on 2020-03-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlocking', '0005_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
