# Generated by Django 3.2.21 on 2023-12-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20230922_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='', upload_to='ad_pictures'),
        ),
    ]
