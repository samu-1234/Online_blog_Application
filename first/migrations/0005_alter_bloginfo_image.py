# Generated by Django 4.0.4 on 2022-06-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_bloginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='image',
            field=models.ImageField(upload_to='./Images'),
        ),
    ]
